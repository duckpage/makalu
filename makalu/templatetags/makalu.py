from django import template
from django.conf import settings
from django.template.defaultfilters import floatformat
 
 
register = template.Library()

@register.filter
def currency(value):
  
  current_currency = 'EUR'
  try:
    current_currency = settings.CURRENCY
  except:
    pass
 
  if value is None:
      value = 0
 
  return '%s %s' % (current_currency, floatformat(value, 2))