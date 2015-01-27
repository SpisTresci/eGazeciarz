from django import template

register = template.Library()


@register.filter(name='zip_tuple')
def zip_tuple(value, arg):
    return value, arg
