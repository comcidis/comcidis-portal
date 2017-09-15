import hashlib
import urllib.parse as urllib
from django import template
from django.utils.safestring import mark_safe
 
register = template.Library()
 
# return only the URL of the gravatar
# TEMPLATE USE:  {{ email|gravatar_url:150 }}
@register.filter
def gravatar_url(email, size=40):
    default = "http://comcidis.lncc.br/static/images/profile.png"
    return "https://www.gravatar.com/avatar/%s?%s" % (hashlib.md5(email.lower().encode("UTF-8")).hexdigest(), urllib.urlencode({'d':default, 's':str(size)}))
