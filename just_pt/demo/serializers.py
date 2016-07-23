from rest_framework import serializers
from demo.models import Message, UserMessage

class MessageSerializer(serializers.Serializer):
	pk = serializers.IntegerField(read_only=True)
	status = serializers.IntegerField(default=0)
	title = serializers.CharField(required=True, allow_blank=False, max_length=100)
	content = serializers.CharField(required=False, allow_blank=True, max_length=1024)

	# category ..
	def create(self, validated_data):
		"""
		 Create and return a new `Message` instance, given the validated data.
		"""
		return Message.objects.create(**validated_data)
	
	def update(self, instance, validated_data):
		"""
		 Update and return an existing `Message` instance, given the validated data.
		"""
		instance.status = validated_data.get('status',instance.status)
		instance.title = validated_data.get('title',instance.title)
		instance.content = validated_data.get('content',instance.content)
		instance.status = validated_data.get('status',instance.status)
		instance.status = validated_data.get('status',instance.status)
		# category

		instance.save()
		return instance

class UserMessageSerializer(serializers.Serializer):
	
	pk = serializers.IntegerField(read_only=True)
	recv_user = serializers.IntegerField()
	send_user = serializers.IntegerField()
	readed = serializers.BooleanField(required=False,default=False)
	status = serializers.IntegerField(default=0)



