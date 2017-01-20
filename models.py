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
    email = db.EmailProperty(required=False)
    created = db.DateTimeProperty(auto_now_add=True)

    @classmethod
    def get_user_by_cookie(cls, cookie):
        if cookie:
            user_id = auth.check_secure_val(cookie)
            if user_id:
                return User.get_by_id(int(user_id))
        return None
