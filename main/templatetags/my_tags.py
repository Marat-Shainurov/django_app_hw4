from django import template
from django.templatetags.static import static

register = template.Library()


@register.simple_tag
def mediapath(path_to_pic):
    return static(path_to_pic)
