from django import template
from django.templatetags.static import static
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def mediapath(path_to_pic):
    return static(path_to_pic)


@register.filter(needs_autoescape=True)
def text_limit_to_display(text, autoescape=True):
    first_hundred = text[:100]
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    result = "%s" % (esc(first_hundred))
    return mark_safe(result)
