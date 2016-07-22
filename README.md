# Run Just Pt
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

###Test models & admin


## Last Mission(Deploy it)

pass


###How to deploy it on pythonanywhere?

pass

### How to deploy it on Heroku ?

pass
