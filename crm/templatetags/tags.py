from django import template
from crm.models import *
from django.contrib.auth.models import User
register = template.Library()
@register.filter(name='no_value')
def no_value(value):
	user = User.objects.get(username=value)
	p = Profile.objects.get(user=user)
	return p.designation

@register.filter(name='phone_value')
def phone_value(value):
	user = User.objects.get(username=value)
	p = Profile.objects.get(user=user)
	return p.user_phone

@register.filter(name='image')
def image(value):
	user = User.objects.get(username=value)
	p = Profile.objects.get(user=user)
	return p.user_photo

@register.filter(name='lead')
def lead(value):
	user = User.objects.get(username=value)
	p = Lead.objects.filter(user=user).count()
	return p

@register.filter(name='won')
def won(value):
	user = User.objects.get(username=value)
	p = Opprtunity.objects.filter(created_by=user,stage="CLOSED WON").count()
	return p

@register.filter(name='lost')
def lost(value):
	user = User.objects.get(username=value)
	p = Opprtunity.objects.filter(created_by=user,stage="CLOSED LOST").count()
	return p


