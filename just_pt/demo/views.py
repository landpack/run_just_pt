from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from demo.models import Message, UserMessage
from demo.serializers import MessageSerializer, UserMessageSerializer

class JSONResponse(HttpResponse):
	"""
	An HttpResponse that renders its content into JSON.
	"""
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def message_list(request):
	"""
	List all message, or create a new message
	"""
	
	if request.method == 'GET':
		message = Message.objects.all()
		serializer = MessageSerializer(message, many=True)
		return JSONResponse(serializer.data)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = MessageSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data, status=201)
		return JSONResponse(serializer.errors, status=400)



@csrf_exempt
def user_message_list(request):
	"""
	List all message, or create a new message
	"""
	
	if request.method == 'GET':
		message = UserMessage.objects.all()
		serializer = UserMessageSerializer(message, many=True)
		return JSONResponse(serializer.data)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = UserMessageSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data, status=201)
		return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def message_manage(request, pk):
	"""
	send message, expect a message format as json like below:
	{
        "category": 3,
        "content": "hello json",
        "status": 0,
        "title": "greet",
	"user":1
	}
	"""
	if request.method == 'GET':
		message = Message.objects.filter(user__id=pk)
		serializer = MessageSerializer(message, many=True)
		return JSONResponse(serializer.data)
	
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = MessageSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data, status=201)
		return JSONResponse(serializer.errors, status=400)



@csrf_exempt
def message_manage_new(request, pk):
	"""
	send message, expect a message format as json like below:
	{
        "category": 3,
        "content": "hello json",
        "status": 0,
        "title": "greet",
	##"user":1 ---> this line are no need anymore.
	##Because, we have add it by the url path ~!~
	##it's very stupid way but work !
	}
	"""
	if request.method == 'GET':
		message = Message.objects.filter(user__id=pk)
		serializer = MessageSerializer(message, many=True)
		return JSONResponse(serializer.data)
	
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		data['user']=pk	# add user id automatic
		serializer = MessageSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data, status=201)
		return JSONResponse(serializer.errors, status=400)







