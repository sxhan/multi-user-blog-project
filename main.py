# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import logging

import jinja2
import webapp2

import auth
import validate
import models

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


class Handler(webapp2.RequestHandler):
    def write(self, *args, **kwargs):
        self.response.out.write(*args, **kwargs)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kwargs):
        logged_in = False
        user_id_cookie = self.request.cookies.get("user_id")
        if user_id_cookie:
            user_id = auth.check_secure_val(user_id_cookie)
            # get our username
            if user_id:
                logged_in = True
        self.write(self.render_str(template,
                                   logged_in=logged_in,
                                   **kwargs))

    def throw_exception(self, code, msg):
        self.response.out.write(str(msg))
        self.response.set_status(int(403))


class MainPage(Handler):

    def get(self):
        self.write("herro")


class SignupHandler(Handler):

    def get(self):
        self.render("signup.html")

    def post(self):

        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email", "")

        is_valid, errors = validate.validate_signup(username=username,
                                                    password=password,
                                                    verify=verify,
                                                    email=email)
        if is_valid:
            # Create new user
            hashed_pw = auth.make_pw_hash(username, password)
            new_user = models.User(username=username,
                                   password=hashed_pw,
                                   email=email)
            new_user.put()
            user_id = new_user.key().id()
            self.response.headers.add_header(
                "Set-Cookie", "user_id=%s; Path=/"
                "" % auth.make_secure_val(user_id))
            self.redirect("/welcome")
        else:
            errors_dict = dict(errors)
            self.render("signup.html",
                        username=username,
                        email=email,
                        **errors_dict)


class WelcomeHandler(Handler):
    @auth.login_required
    def get(self):
        # self.response.headers["Content-Type"] = "text/plain"
        user_id_cookie = self.request.cookies.get("user_id")
        if user_id_cookie:
            user_id = auth.check_secure_val(user_id_cookie)
            # get our username
            if user_id:
                username = models.User.get_by_id(int(user_id)).username
            else:
                username = ""

            self.render("welcome.html", username=username)
        else:
            self.redirect("/signup")


class LoginHandler(Handler):
    def get(self):
        self.render("login.html")

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")

        is_valid, errors = validate.validate_login(username=username,
                                                   password=password)
        if is_valid:
            logging.info("username: %s" % username)
            user = models.User.all().filter("username =", username).get()
            user_id = user.key().id()
            logging.info("user id: %s" % user_id)
            self.response.headers.add_header(
                "Set-Cookie",
                "user_id=%s; Path=/" % auth.make_secure_val(user_id))
            self.redirect("/welcome")
        else:
            errors_dict = dict(errors)
            self.render("login.html",
                        username=username,
                        password=password,
                        **errors_dict)


class LogoutHandler(Handler):
    def get(self):
        user_id_cookie = self.request.cookies.get("user_id")
        if user_id_cookie:
            self.response.headers.add_header(
                "Set-Cookie", "user_id=; Path=/")
            self.redirect("/signup")
        else:
            self.redirect("/signup")
        return


class BlogFrontPage(Handler):

    def get(self):
        posts = models.BlogPost.all().order('-created')
        self.render("front.html",
                    posts=posts)


class NewPostHandler(Handler):

    def render_front(self, subject="", content="", error=""):
        self.render("newpost.html",
                    subject=subject, content=content, error=error)

    @auth.login_required
    def get(self):
        self.render_front()

    @auth.login_required
    def post(self):
        subject = self.request.get("subject")
        content = self.request.get("content")

        # since theres a login_required decorator, the user must exist
        user = models.User.get_user_by_cookie(
            self.request.cookies.get("user_id"))

        if subject and content:
            a = models.BlogPost(subject=subject,
                                content=content,
                                author=user.username)
            a.put()
            self.redirect("/blog/" + str(a.key().id()))
            # self.render_front()
        else:
            error = "we need subject and content!"
            self.render_front(subject=subject, content=content, error=error)


class BlogPostHandler(Handler):

    def get(self, post_id):
        post = models.BlogPost.get_by_id(int(post_id))
        self.render("permalink.html", post=post)


class EditBlogPostHandler(Handler):

    @auth.login_required
    def get(self, post_id):
        # Check whether the correct user is accessing this page
        post = models.BlogPost.get_by_id(int(post_id))
        user = models.User.get_user_by_cookie(
            self.request.cookies.get("user_id"))

        if post and user and user.is_owner(post):
            self.render("editpost.html", post=post)
        else:
            self.throw_exception(403,
                                 "you are not authorized to perform this "
                                 "action!")

    @auth.login_required
    def post(self, post_id):
        # Check whether the correct user is accessing this page
        post = models.BlogPost.get_by_id(int(post_id))
        user = models.User.get_user_by_cookie(
            self.request.cookies.get("user_id"))
        if not (post and user and user.is_owner(post)):
            self.throw_exception(403,
                                 "you are not authorized to perform this "
                                 "action!")
            return

        # Update object
        subject = self.request.get("subject")
        content = self.request.get("content")

        # # since theres a login_required decorator, the user must exist
        # user = models.User.get_user_by_cookie(
        #     self.request.cookies.get("user_id"))

        if subject and content:
            post = models.BlogPost.get_by_id(int(post_id))
            post.subject = subject
            post.content = content
            post.put()
            self.redirect("/blog/" + str(post.key().id()))
            # self.render_front()
        else:
            error = "we need subject and content!"
            self.render("newpost.html",
                        subject=subject, content=content, error=error)


class DeleteBlogPostHandler(Handler):

    @auth.login_required
    def post(self, post_id):
        post = models.BlogPost.get_by_id(int(post_id))
        post.delete()
        self.redirect("/blog")


class VoteHandler(Handler):

    def _vote(self, post_id, vote_val):
        post = models.BlogPost.get_by_id(int(post_id))
        user = models.User.get_user_by_cookie(
            self.request.cookies.get("user_id"))
        if post and user and user.is_owner(post):
            self.throw_exception(403,
                                 "You cannot vote on your own posts!")
        else:
            user_id = user.key().id()
            post_id = post.key().id()
            # Search for existing likes
            existing = models.Vote.all().filter("user_id =", user_id) \
                .filter("blog_post_id =", post_id)

            # Create new vote
            if existing.count() == 0:
                vote = models.Vote(blog_post_id=post_id,
                                   user_id=user_id,
                                   score=int(vote_val))

            # If new vote is same as old vote, undo old vote (set to 0).
            # If new vote is different form old vote, update old vote.
            else:
                vote = existing.get()
                if vote.score == int(vote_val):
                    vote.score == 0
                else:
                    vote.score = int(vote_val)

            vote.put()

            # Redirect to referring page
            referrer = self.request.headers.get('referer')
            if referrer:
                return self.redirect(referrer)
            return self.redirect_to('/blog')


class UpvoteHandler(VoteHandler):

    @auth.login_required
    def post(self, post_id):
        self._vote(post_id, 1)


class DownvoteHandler(VoteHandler):

    @auth.login_required
    def post(self, post_id):
        self._vote(post_id, -1)


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/welcome', WelcomeHandler),
    ('/signup', SignupHandler),
    ('/login', LoginHandler),
    ('/logout', LogoutHandler),
    ('/blog/?', BlogFrontPage),
    ('/blog/([0-9]+)', BlogPostHandler),
    ('/blog/([0-9]+)/edit', EditBlogPostHandler),
    ('/blog/([0-9]+)/delete', DeleteBlogPostHandler),
    ('/blog/([0-9]+)/up', UpvoteHandler),
    ('/blog/([0-9]+)/down', DownvoteHandler),
    ('/blog/newpost', NewPostHandler)],
    debug=True)
