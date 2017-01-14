from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.filter
@register.inclusion_tag('simplepush.html', takes_context=True)
def simplepush_html(context):
    request = context['request']
    return {'request': request}


@register.filter
@register.inclusion_tag('simplepush_button.html', takes_context=True)
def simplepush_html_button(context):
    url = reverse('save_simplepush_info')
    request = context['request']
    return {'url': url, 'request': request}