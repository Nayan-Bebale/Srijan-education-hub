from django.contrib import admin
from django.urls import path, include
from .views import chatapp

app_name = 'chatsystem'

urlpatterns = [
    path('chat/', chatapp, name='chatapp')
] 