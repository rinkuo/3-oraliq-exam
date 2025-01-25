# posts/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def color_for_index(value):
    colors = ["red", "blue", "green", "yellow", "purple", "orange"]
    try:
        return colors[value % len(colors)]
    except IndexError:
        return 'gray'
