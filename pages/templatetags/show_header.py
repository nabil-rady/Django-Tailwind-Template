from django import template

register = template.Library()

@register.inclusion_tag('pages/header.html')
def show_header():
    return {}