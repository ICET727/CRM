import asyncio
from channels.generic.websocket import AsyncJsonWebsocketConsumer
#from channels.consumer import AsyncConsumer
from .models import Meeting
from datetime import datetime

now = datetime.now()
#last_day = datetime.strftime(datetime.now() + timedelta(1), '%Y-%m-%d')
class NoseyConsumer(AsyncJsonWebsocketConsumer):
	async def connect(self):
		await self.accept()
		await self.channel_layer.group_add("gossip", self.channel_name)
		#print(f"Added {self.channel_name} channel to gossip")

	async def disconnect(self):
		await self.channel_layer.group_discard("gossip", self.channel_name)
		#print(f"Removed {self.channel_name} channel from gossip")

	async def user_gossip(self, event):
		await self.send_json(event)
		#print(f"Got message {event} at {self.channel_name}")


class Echoconsumer(AsyncJsonWebsocketConsumer):
	async def connect(self):
		await self.accept()
		data = Meeting.objects.filter(date=now.date())
		l = []
		t = []
		for i in data:
			l.append(i.name)
			t.append(str(i.time))
		await self.send_json({"name":len(l),"time1":t})