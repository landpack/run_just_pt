from django.contrib import admin

# Register your models here.

from .models import Message, UserMessage

admin.site.register(Message)
admin.site.register(UserMessage)

