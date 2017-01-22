from google.appengine.ext import db

import auth


class BlogPost(db.Model):
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    author = db.StringProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)


class User(db.Model):
    username = db.StringProperty(required=True)
    password = db.StringProperty(required=True)
    email = db.StringProperty(required=False)
    created = db.DateTimeProperty(auto_now_add=True)

    @classmethod
    def get_user_by_cookie(cls, cookie):
        """Returns User object given a user_id cookie string. Returns None if
        something fails in the process
        """
        if cookie:
            user_id = auth.check_secure_val(cookie)
            if user_id:
                return User.get_by_id(int(user_id))
        return None

    def is_owner(self, post):
        if self.username == post.author:
            return True
        else:
            return False


class Vote(db.Model):
    blog_post_id = db.IntegerProperty(required=True)
    user_id = db.IntegerProperty(required=True)
    score = db.IntegerProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
