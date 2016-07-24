# Run Just Pt
This is a demo for test the personal ability by the PuTao  ,There are only two point I need to do but I attachment one (deploy it to cloudy) myself.


##Questions
* 1.How to configure the environment ?
* 2.How to create APIs according the models declare ?

##Solutions
####Part one
---
To configure our env, just simple run both command example `virtualenv` and `pip`. To run the demo , must do some debug and configure the demo base setting and do some init with the database.

###Part two
---
* 1.send message from front-tool, so I pick up `httpie`
* 2.to list the message which belong some body, just simple need a query command. on django ORM, it's should be like  `Message.objects.filter(user__id=1)`
* 3.to list the message by separate page,this is call paginate.(On the SQL database,just a `limit` command)
* 4.to delete a message by id,it's also very simple, to make it clear just run two query. example: `message=Message.objects.filter(user__id=1)
 message.delete()`


##Do 

###First Mission (configure env)
---
```
git clone https://github.com/landpack/run_just_pt.git
cd run_just_pt
virtualenv putaoEnv
source ./putaoEnv/bin/activate
pip install django
cp -r ~/Desktop/just_pt/ ./just_pt
```
###Second Mission (make it work)
---

####Try to run it.
Now, I can focus on the project! First at first, let's try to run the project without any modify, see everything work fine!

```
cd just_pt
python manage.py runserver
```
Now that the server’s running, I can visit http://127.0.0.1:8000/ with my Web browser!

####Do some anlysis

Normally, there few file should be inside the `demo` file, but the `PuTao` remove some, What we missed?

* 1.The `urls.py`
* 2.The `apps.py`
* 3.The `admin.py`
* 4.The `views.py`
* 5.The `tests.py`

To install the `demo` app on the project, just simple configure it on the `settings.py` and then write a `apps.py` inside to the `demo`. 

demo/apps.py

```
from django.apps import AppConfig


class DemoConfig(AppConfig):
    name = 'demo'

```

To manage the demo models easy, I just simple register it   into the admin. 


```
from django.contrib import admin

from .models import Message, UserMessage
admin.site.register(Message)
admin.site.register(UserMessage)

```
Now, Just run the `python manage.py makemigrations demo`, if everything work ok, congratulation, you keep going. But, it's impossible, the `just_pt` project is Bug-Box,you should move the inside `just_pt/just_pt/demo` out  to `just_pt/demo`, and then run the `makemigration` again. if everthing work for you (Haha, it's work for me), try the `python manage.py migrate` to make write to the `sqlite` database.

###Create super user
---
This is very easy to create a superuser, if you work with  `flask` you be sadly ...

```
python manage.py createsuperuser
```
Hit enter, and then follow promt expect you input some personal information , like your name, password, email, just input will fine :)

Test models & admin

###Create api with Rest framework!
---
To make the list have a certain order,I just simple modify the `demo/models.py` by add the below line.

```
class Meta:
    ordering = ('create_time',)

```

####How to install Rest Framework?

Just only one line command...
```
pip install djangorestframework
```

####How to install the Rest-Framework App to our project?

It's also simple,just put the below line into the django `settings.py` fiel.

```
INSTALL_APPS = (
	'rest_framework',
	# rest of other code ...& app
)
```
####Create a Serializer class.

>The first thing we need to get started on our Web API is to provide a way of serializing and deserializing the snippet instances into representations such as json. We can do this by declaring serializers that work very similar to Django's forms. Create a file in the snippets directory named serializers.py and add the following.

According the docs, we can follow it and just simple modify something,it's will work for me. So, I create a file in the `demeo` directory named `serializers.py` .
run `git checkout v0.2` can see it.


####Create Serializer By ModelSerializer

Some one have a old said, a good programmer should not be repeat itself! so , I will show you how to use `ModelSerializer`, run `git chekcout v0.3` see current version.

####writing regular django views using our serializer
It's time to show our API to the public, so write some view function to `demo/views.py` to get currently code, go an run `git checkout v0.4`

####To test APi by a tool name `http`

simple install it by the below comamnd

```
pip install httpie
```
When you wake up your server by the follow command

```
python manage.py runserver
```
and then open a new terminal windows, run the below command.

```
http http://127.0.0.1:8000/demo/api/
```
output should be like the below ..(for me)

```
TTP/1.0 200 OK
Content-Type: application/json
Date: Sat, 23 Jul 2016 07:39:17 GMT
Server: WSGIServer/0.1 Python/2.7.10
X-Frame-Options: SAMEORIGIN

[
    {
        "category": 1, 
        "content": "hello", 
        "id": 1, 
        "status": 0, 
        "title": "frank"
    }, 
    {
        "category": 0, 
        "content": "hello landpack", 
        "id": 2, 
        "status": 0, 
        "title": "greet"
    }, 
    {
        "category": 0, 
        "content": "hello landpack", 
        "id": 3, 
        "status": 0, 
        "title": "greet"
    }
]
```
Currently version of my code, can run `git checkout v0.5` to get it.

###Make more API & Make version tag to the API
---
Because the api should be change as the time goes and the requirement being change, so have version control is good idea. it's simple just do some change to the `demo/urls.py`

```
 url(r'^api/v0.1/message_list$',views.message_list),
 
```
Okay , let's add api to transer data with UserMessage class. Okay, keep test our api, first let's test `POST` method.

I have write simple sample json file name as sample.json

```
   {
        "category": 3, 
        "content": "hello json", 
        "status": 0, 
        "title": "greet"
    }

```

quit your editer and save it to the root directory of project, and then run the below code to `POST` it to the server.

```
http POST http://127.0.0.1:8000/demo/api/v0.1/message_list @sample.json
```
I you done, you should see the below output.

```
HTTP/1.0 201 Created
Content-Type: application/json
Date: Sat, 23 Jul 2016 10:55:06 GMT
Server: WSGIServer/0.1 Python/2.7.10
X-Frame-Options: SAMEORIGIN

{
    "category": 3, 
    "content": "hello json", 
    "id": 5, 
    "status": 0, 
    "title": "greet"
}
```
Try `git checkout v0.6` to current version.

To test another api ,just do the same, cause we are going to have two test json file, so i rename the sample.json to message_sample.json and then add a new file name as user_message_sample.json for test another api.

It's also simple, just run the below command:

```
http POST http://127.0.0.1:8000/demo/api/v0.1/user_message_list @user_message_sample.json
```
BTW,my test work fine,I no going to put the result there.
Try `git checkout v0.6a ` to get current version.

###Show Message filter by User
---
To get the message which belong someone, just simple call  Django ORM with a filter function. I will implement it with `api version 2`

###Fix the model logic
---
I don't why, but I feel the `UserMessage` should no have a ForeignKey, I think the ForeignKey should be inside the Message class. so I do some modify. add the below line into the Message class.

```
user = models.ForeignKey('UserMessage', null=True,blank=True)

```
Now, just run migrate , do below command

```
python manage.py makemigrations demo
python manage.py migrate
```
You can play with shell now!

```
>>> from demo.models import UserMessage,Message
>>> u=UserMessage(recv_user=110)
>>> u.save()
>>> u
<UserMessage: User ID 8>
>>> u.message_set
<django.db.models.fields.related_descriptors.RelatedManager object at 0x107822810>
>>> u.message_set.all()
[]

```
Hey, the User ID is 8, it's because I have delete de database for now! I just change the database structure.
you can see current user have no message! so let's add some message to our user.

```
>> m=Message(title='hello, django',user=u)
>>> m.save()
>>> m=Message(title='good bye, flask',user=u)
>>> m.save()
>>> u.message_set.all()
[<Message: hello, django>, <Message: good bye, flask>]

```

HaHa, we got all message belong to the user. `git checkout v0.7` to here.To show how to show the target message which relay on the user id, I do the follwoing play with the shell.

```
>>> from demo.models import Message,UserMessage
>>> m=Message.objects.all()
>>> m
[]
>>> m=Message(title='first message')
>>> m.save()
>>> m
<Message: first message>
>>> UserMessage.objects.all()
[]
>>> u=UserMessage(recv_user=110,send_user=120)
>>> u.save()
>>> u
<UserMessage: User ID 1>
>>> m=Message(title='second message',user=u)
>>> m.save()
>>> u2=UserMessage(recv_user=119,send_user=911)
>>> u2.save()
>>> m2=Message(title='hey, this second user  message',user=u2)
>>> m2.save()
>>> Message.objects.filter(user__id=1)
[<Message: second message>]
>>> Message.objects.filter(user__id=2)
[<Message: hey, this second user  message>]
>>> 

```
At the end, i have query the target message by the user id, it's pretty simple.but how to change the current version of api! keep going.there are serveral file we need to modify.

```
def message_manage(request, pk):
	pass
```
and then map our new view funtion to the `demo/urls.py` to let the project know it exists.

```
url(r'^api/v0.2/message_manage/(?P<pk>[0-9]+)/$', views.message_manage),
```
okay, it's time to test our code for now! First at first run the server, and then use the `http` tool to visite our api, let's see my output .

```
(putaoEnv)mysite $http http://127.0.0.1:8000/demo/api/v0.2/message_manage/2/
HTTP/1.0 200 OK
Content-Type: application/json
Date: Sun, 24 Jul 2016 03:17:34 GMT
Server: WSGIServer/0.1 Python/2.7.10
X-Frame-Options: SAMEORIGIN

[
    {
        "category": 0, 
        "content": null, 
        "id": 3, 
        "status": 0, 
        "title": "hey, this second user  message", 
        "user": 2
    }
]

(putaoEnv)mysite $http http://127.0.0.1:8000/demo/api/v0.2/message_manage/1/
HTTP/1.0 200 OK
Content-Type: application/json
Date: Sun, 24 Jul 2016 03:17:39 GMT
Server: WSGIServer/0.1 Python/2.7.10
X-Frame-Options: SAMEORIGIN

[
    {
        "category": 0, 
        "content": null, 
        "id": 2, 
        "status": 0, 
        "title": "second message", 
        "user": 1
    }
]



```

Now, let's test out api with `POST` method. to test the `POST` method , you have to create some test data fromat as JSON, I show you my example data below:

``` 
{
        "category": 0, 
        "content": null, 
        "id": 2, 
        "status": 0, 
        "title": "flask is to light even can fly", 
        "user": 1
}
```
You can see i have add three message to our user with id is '1',so let's post it with our http tool run the below command.

```
http POST http://127.0.0.1:8000/demo/api/v0.2/message_manage/2/ @message_manage_sample.json
```
And then you can see the output below.

```
HTTP/1.0 201 Created
Content-Type: application/json
Date: Sun, 24 Jul 2016 03:27:41 GMT
Server: WSGIServer/0.1 Python/2.7.10
X-Frame-Options: SAMEORIGIN

{
    "category": 0, 
    "content": null, 
    "id": 4, 
    "status": 0, 
    "title": "flask is to light even can fly", 
    "user": 1
}
```
Okay, seems everything work good, but I gotta sadly tell you i have make a bug, it's doesn't best. Let me show the  http request command again.

```
http POST http://127.0.0.1:8000/demo/api/v0.2/message_manage/2/ @message_manage_sample.json
```
it's has point to `~/message_manage/2/` ,it's mean I should post the data to a user with id is '2',but i can post data to user with id is '1'. how to fixed it, just follow . 


###Write a new version api


###Remove the sqlite & create superuser again.
---
I guess there are have some logic design bug of the models, so i decide to rewrite the models migrate to the db.to make a message connect with a user id, i should do some change with the models again.

```
>>> from demo.serializers import MessageSerializer
>>> from rest_framework.renderers import JSONRenderer
>>> from rest_framework.parsers import JSONParser
>>> message=Message(title='rest api is boring')
>>> message.save()
>>> message
<Message: rest api is boring>
>>> serializer=MessageSerializer(message)
>>> serializer.data
{'status': 0, 'category': 0, 'title': u'rest api is boring', 'content': None, 'user': None, 'id': 5}
>>> serializer.data['user']=1	# no act work!!
>>> serializer.data
{'status': 0, 'category': 0, 'title': u'rest api is boring', 'content': None, 'user': None, 'id': 5}
>>> serializer.data['user']
>>> ss=serializer.data
>>> ss
{'status': 0, 'category': 0, 'title': u'rest api is boring', 'content': None, 'user': None, 'id': 5}
>>> ss['user']=1
>>> ss
{'status': 0, 'category': 0, 'title': u'rest api is boring', 'content': None, 'user': 1, 'id': 5}
>>> 

```
It's seems very good ideas, but when i run the below code.

```
>>> ss.save()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'ReturnDict' object has no attribute 'save'
```
I have get the user id from url , but i can't update the message user field to the JSON response, how should i do?
just keep ..

As we know, we add new item to the server by api is `POST` method, in the `POST` block, we have data from request with JSONParser return , so let's think a moment. can we change the source data , and then serializer it .

```
 #rest of the code 
elif request.method == 'POST':
                data = JSONParser().parse(request)
                data['user']=pk # add user id automatic

 #rest of code
```

to resgiter our view function, just do some change on the `demo/urls.py` the code below.

```
url(r'^api/v0.3/message_manage/(?P<pk>[0-9]+)/$', views.message_manage_new),
```

and then test our new api, with `http` tool. First at first, test it with `GET` method.

```
(putaoEnv)just_pt $http http://127.0.0.1:8000/demo/api/v0.3/message_manage
/2/
HTTP/1.0 200 OK
Content-Type: application/json
Date: Sun, 24 Jul 2016 10:05:28 GMT
Server: WSGIServer/0.1 Python/2.7.10
X-Frame-Options: SAMEORIGIN

[
    {
        "category": 0, 
        "content": null, 
        "id": 3, 
        "status": 0, 
        "title": "hey, this second user  message", 
        "user": 2
    }
]

```
Now, see our test sample json data below:

```
  {
        "category": 0,
        "content": null,
        "id": 2,
        "status": 0,
        "title": "django is bad idea to  write a API", 
    }
```

Okay, time to test our `POST` method, do it with follow command:

```
(putaoEnv)just_pt $http http://127.0.0.1:8000/demo/api/v0.3/message_manage
/2/
```

Now, you can see the output ,I do both test `GET` & `POST` ,to git current version, got `git checkout v0.8`

```
HTTP/1.0 200 OK
Content-Type: application/json
Date: Sun, 24 Jul 2016 10:10:02 GMT
Server: WSGIServer/0.1 Python/2.7.10
X-Frame-Options: SAMEORIGIN

[
    {
        "category": 0, 
        "content": null, 
        "id": 3, 
        "status": 0, 
        "title": "hey, this second user  message", 
        "user": 2
    }, 
    {
        "category": 0, 
        "content": null, 
        "id": 6, 
        "status": 0, 
        "title": "flask is to light even can fly", 
        "user": 2
    }
]

```

Now, let's review the question, we just need to list the message which mark as unremove-message.so we need to do some filter before we show it. let's play it with shell.

```
>>> Message.objects.filter(user__id=1,status=0)
[<Message: second message>, <Message: flask is to light even can fly>]
>>> from demo.models import Message
>>> Message.objects.filter(user__id=1,status=0)
[<Message: second message>, <Message: flask is to light even can fly>]
>>> Message.objects.filter(user__id=1,status=1)
[]
```
Now, it's time to rewrite the `demo/views.py` again.


```
@csrf_exempt
def message_manage_v4(request, pk):
 #Rest of code ...
 if request.method == 'GET':
                message = Message.objects.filter(user__id=pk, status=0)

```

And now, just register it inside the `demo/urls.py` again! it's boring , right?  ~!~ But this it job!


```
urlpatterns = [

 #rest the of code ...
        url(r'^api/v0.4/message_manage/(?P<pk>[0-9]+)/$', views.message_man
age_v4),
]
```

Now,test my api version 0.4 ,The current test data show as below.

```
  {
        "category": 0,
        "content": null,
        "id": 2,
        "status": 1,
        "title": "hey, this message should no show"                       
    }

```
Okay, try the super tool `http`,and then do the follow command.

step one, check our database with api. the result show below.

```
(putaoEnv)just_pt $http http://127.0.0.1:8000/demo/api/v0.4/message_manage
/1/
HTTP/1.0 200 OK
Content-Type: application/json
Date: Sun, 24 Jul 2016 16:59:20 GMT
Server: WSGIServer/0.1 Python/2.7.10
X-Frame-Options: SAMEORIGIN

[
    {
        "category": 0, 
        "content": null, 
        "id": 2, 
        "status": 0, 
        "title": "second message", 
        "user": 1
    }, 
    {
        "category": 0, 
        "content": null, 
        "id": 4, 
        "status": 0, 
        "title": "flask is to light even can fly", 
        "user": 1
    }
]

```

step two, post some new data, but the message status set to 1.

```
(putaoEnv)just_pt $http POST http://127.0.0.1:8000/demo/api/v0.4/message_m
anage/1/ @message_manage_new_sample.json
HTTP/1.0 201 Created
Content-Type: application/json
Date: Sun, 24 Jul 2016 16:58:39 GMT
Server: WSGIServer/0.1 Python/2.7.10
X-Frame-Options: SAMEORIGIN

{
    "category": 0, 
    "content": null, 
    "id": 7, 
    "status": 1, 
    "title": "hey, this message should no show", 
    "user": 1
}

```
 
Okay, we can test why the new data can show .

```

(putaoEnv)just_pt $http http://127.0.0.1:8000/demo/api/v0.4/message_manage
/1/
HTTP/1.0 200 OK
Content-Type: application/json
Date: Sun, 24 Jul 2016 17:02:36 GMT
Server: WSGIServer/0.1 Python/2.7.10
X-Frame-Options: SAMEORIGIN

[
    {
        "category": 0, 
        "content": null, 
        "id": 2, 
        "status": 0, 
        "title": "second message", 
        "user": 1
    }, 
    {
        "category": 0, 
        "content": null, 
        "id": 4, 
        "status": 0, 
        "title": "flask is to light even can fly", 
        "user": 1
    }
]


```
Okay, i have finish the current tag, it's pretty cool.to get the current version, run `git checkout v0.9` .

```
(putaoEnv)just_pt $http http://127.0.0.1:8000/demo/api/v0.4/message_manage/1/
HTTP/1.0 200 OK
Content-Type: application/json
Date: Sun, 24 Jul 2016 17:37:05 GMT
Server: WSGIServer/0.1 Python/2.7.10
X-Frame-Options: SAMEORIGIN

[
    {
        "category": 0, 
        "content": null, 
        "id": 2, 
        "status": 0, 
        "title": "second message", 
        "user": 1
    }, 
    {
        "category": 0, 
        "content": null, 
        "id": 4, 
        "status": 0, 
        "title": "flask is to light even can fly", 
        "user": 1
    }
]

(putaoEnv)just_pt $http DELETE http://127.0.0.1:8000/demo/api/v0.4/message_manage/4/delete
HTTP/1.0 204 No Content
Content-Length: 0
Content-Type: text/html; charset=utf-8
Date: Sun, 24 Jul 2016 17:37:42 GMT
Server: WSGIServer/0.1 Python/2.7.10
X-Frame-Options: SAMEORIGIN



(putaoEnv)just_pt $http http://127.0.0.1:8000/demo/api/v0.4/message_manage/1/
HTTP/1.0 200 OK
Content-Type: application/json
Date: Sun, 24 Jul 2016 17:37:49 GMT
Server: WSGIServer/0.1 Python/2.7.10
X-Frame-Options: SAMEORIGIN

[
    {
        "category": 0, 
        "content": null, 
        "id": 2, 
        "status": 0, 
        "title": "second message", 
        "user": 1
    }
]


```
I dont want to say any word, just see the result put at below.got `git checkout v1.0`

Sadly, I have no time to implement the pagination for now ~!~ 


##Attachment


###Api & Memcached
---
pass


### Last Mission(Deploy it)
---
pass


####How to deploy it on pythonanywhere?

pass

#### How to deploy it on Heroku ?

pass
