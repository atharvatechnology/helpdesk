from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name="has_group")
def has_group(user, group_name):
    print("ff",user.groups.all().filter(name=group_name).exists())
    return user.groups.all().filter(name=group_name).exists()

