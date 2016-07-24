from django.conf.urls import url
from demo import views

urlpatterns = [

	url(r'^api/v0.1/message_list$',views.message_list),
	url(r'^api/v0.1/user_message_list$',views.user_message_list),
	url(r'^api/v0.2/message_manage/(?P<pk>[0-9]+)/$', views.message_manage),
]
