from rest_framework import serializers
from demo.models import Message, UserMessage

class MessageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Message
		fields = ('id','status','title','content','category')

class UserMessageSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserMessage
		fields = ('id','recv_user','send_user','readed','status')


