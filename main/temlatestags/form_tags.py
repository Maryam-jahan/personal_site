from django import template

register = template.library()

@register.filter(name='add_class')
def add_class(field, css):
    return field.as_widgt(attrs={'class':css})