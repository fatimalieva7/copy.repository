
from goods.models import Categories
from django import template
from django.utils.http import urlencode


register = template.Library()

@register.simple_tag()
def tag_categories():
    return Categories.objects.all()

@register.simple_tag(takes_context=True)

def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    if kwargs.get('page') is None:
        kwargs.pop('page', None)

    query.update(kwargs)
    query =  urlencode(query)
    return '?' + query if query else '' 
