from rest_framework import serializers
from .models import *

class EmailSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	sender = serializers.EmailField()
	Subject = serializers.CharField(required=False, allow_blank=True, max_length=100)
	Body = serializers.CharField(max_length=5000)
	file = serializers.FileField()

	def create(self,validate_data):
		return Email.objects.create(**validate_data)


class ProductSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Product
		fields =  '__all__' #['name','price','solubility','HSN_Number']


class MeetingSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField(required=False, allow_blank=True, max_length=100)
	date = serializers.DateField()#auto_now=True)
	time = serializers.TimeField()#auto_now=False, auto_now_add=False)
	description = serializers.CharField(max_length=1000)

	def create(self,validate_data):
		return Meeting.objects.create(**validate_data)

class TaskSerializer(serializers.Serializer):
	class Meta:
		model = Task
		fields = '__all__'


class OpportunitySeriaizer(serializers.Serializer):
	class Meta:
		model = Opprtunity
		fields = '__all__'

class LeadSerializer(serializers.Serializer):
	class Meta:
		model = Lead
		fields = '__all__'