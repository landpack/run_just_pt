## Run Just Pt
This is a demo for test the personal ability by the PuTao  ,There are only two point I need to do but I attachment one (deploy it to cloudy) myself.

* 1.How to configure the environment.
* 2.Do some define & http request according the models declare.
* 3.Deploy it to cloudy.

##First Mission (configure env)

```
git clone https://github.com/landpack/run_just_pt.git
cd run_just_pt
virtualenv putaoEnv
source ./putaoEnv/bin/activate
pip install django
cp -r ~/Desktop/just_pt/ ./just_pt
```
##Second Mission (make it work)
---

###Try to run it.
Now, I can focus on the project! First at first, let's try to run the project without any modify, see everything work fine!

```
cd just_pt
python manage.py runserver
```
Now that the server’s running, I can visit http://127.0.0.1:8000/ with my Web browser!

###Do some anlysis

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

This is very easy to create a superuser, if you work with  `flask` you be sadly ...

```
python manage.py createsuperuser
```
Hit enter, and then follow promt expect you input some personal information , like your name, password, email, just input will fine :)
Test models & admin

##Create api with Rest framework!
To make the list have a certain order,I just simple modify the `demo/models.py` by add the below line.

```
class Meta:
    ordering = ('create_time',)

```

###How to install Rest Framework?

Just only one line command...
```
pip install djangorestframework
```

###How to install the Rest-Framework App to our project?

It's also simple,just put the below line into the django `settings.py` fiel.

```
INSTALL_APPS = (
	'rest_framework',
	# rest of other code ...& app
)
```
###Create a Serializer class.

>The first thing we need to get started on our Web API is to provide a way of serializing and deserializing the snippet instances into representations such as json. We can do this by declaring serializers that work very similar to Django's forms. Create a file in the snippets directory named serializers.py and add the following.

According the docs, we can follow it and just simple modify something,it's will work for me. So, I create a file in the `demeo` directory named `serializers.py` .
run `git checkout v0.2` can see it.


###Create Serializer By ModelSerializer

Some one have a old said, a good programmer should not be repeat itself! so , I will show you how to use `ModelSerializer`, run `git chekcout v0.3` see current version.

###writing regular django views using our serializer
It's time to show our API to the public, so write some view function to `demo/views.py` to get currently code, go an run `git checkout v0.4`

###To test APi by a tool name `http`

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
To get the message which belong someone, just simple call  Django ORM with a filter function. I will implement it with `api version 2`

###Fix the model logic
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

HaHa, we got all message belong to the user. `git checkout v0.7` to here.

##Api & Memcached

pass


## Last Mission(Deploy it)

pass


###How to deploy it on pythonanywhere?

pass

### How to deploy it on Heroku ?

pass
