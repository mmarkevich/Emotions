from django.urls import path
from . import views
from .views import UserView, VideoInformationSerializerView, DataAboutUserAndVideoSerializerView



urlpatterns = [
path('test', UserView.as_view()),
path('test2', VideoInformationSerializerView.as_view()),
path('test3', DataAboutUserAndVideoSerializerView.as_view()),
path ('registration', views.registration, name='registration'),
path('video_list', views.video_list, name='video_list')
]