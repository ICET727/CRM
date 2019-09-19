from .models import *
#from django.contrib.auth.models import User
#from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from datetime import datetime

now = datetime.now()

@receiver(post_save, sender=Case)
def announce_new_case(sender, instance, created, **kwargs):
	if created:
		channel_layer = get_channel_layer()
		#print(get_channel_layer())
		#print("Hii")
		#print(instance)
		#user = get_user_model()
		#print(user)
		async_to_sync(channel_layer.group_send)(
			"gossip",{
				"type": "user.gossip",
				"event": "Case",
				"sales_person" : "Case",
				"case_date": str(instance.date),
				"customer": instance.case_lead.lead_company,
			}
			)




@receiver(post_save, sender=Order)
def announce_new_order(sender, instance, created, **kwargs):
	if created:
		#print("Hii")
		channel_layer = get_channel_layer()
		async_to_sync(channel_layer.group_send)(
			"gossip",{
				"type":"user.gossip",
				"event":"Order",
				"sales_person": instance.sales_member.first_name,
				"amount":instance.total_amount,
				"customer":instance.order_lead.lead_company,
				"date":str(instance.created_on),
			}
			)

