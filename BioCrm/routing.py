from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

#from crm.consumers import TickTockConsumer  
from crm.consumers import NoseyConsumer, Echoconsumer



application = ProtocolTypeRouter({
	"websocket": URLRouter([
		path("ws/", Echoconsumer),
		#path("meetings/", MeetingConsumer),
		path("notifications/", NoseyConsumer),
		])
	})