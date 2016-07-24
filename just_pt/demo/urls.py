from django.conf.urls import url
from demo import views

urlpatterns = [

	url(r'^api/v0.1/message_list$',views.message_list),
	url(r'^api/v0.1/user_message_list$',views.user_message_list),
	url(r'^api/v0.2/message_manage/(?P<pk>[0-9]+)/$', views.message_manage),
	url(r'^api/v0.3/message_manage/(?P<pk>[0-9]+)/$', views.message_manage_new),
	url(r'^api/v0.4/message_manage/(?P<pk>[0-9]+)/$', views.message_manage_v4),
]
