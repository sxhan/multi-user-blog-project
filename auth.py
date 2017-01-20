import hmac
from functools import wraps

from lib.bcrypt import bcrypt


SECRET = "THISISSOSECRET"


def hash_str(s):
    return hmac.new(SECRET, s).hexdigest()


def make_secure_val(s):
    s = str(s)
    return "%s|%s" % (s, hash_str(s))


def check_secure_val(h):
    val = h.split("|")[0]
    if h == make_secure_val(val):
        return val
    else:
        return None


def make_pw_hash(username, password, salt=None):
    if salt is None:
        salt = bcrypt.gensalt()
    h = bcrypt.hashpw(username + password, salt)
    return "%s|%s" % (h, salt)


def login_required(f):
    @wraps(f)
    def wrapper(self, *args, **kwargs):
        user_id_cookie = self.request.cookies.get("user_id")
        if user_id_cookie:
            user_id = check_secure_val(user_id_cookie)
            if user_id:
                return f(self, *args, **kwargs)
            else:
                return self.redirect("/login")
        else:
            return self.redirect("/login")
    return wrapper
