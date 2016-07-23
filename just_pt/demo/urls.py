from django.conf.urls import url
from demo import views

urlpatterns = [

	url(r'^api/$',views.message_list),
]
