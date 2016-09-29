from hashlib import md5
from django import template

register = template.Library()


@register.filter(name='gravatar')
def gravatar(user, size=100):
    email = str(user.email.strip().lower()).encode('utf-8')
    email_hash = md5(email).hexdigest()
    url = "//www.gravatar.com/avatar/{0}?s={1}&d=identicon&r=PG&d=retro"
    return url.format(email_hash, size)