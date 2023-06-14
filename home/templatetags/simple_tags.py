from django.template import Library
from home.models import Category
from home.forms import SubscribeForm

register = Library()

@register.simple_tag
def global_form():
    return SubscribeForm()


@register.simple_tag
def global_category():
    return Category.objects.all()