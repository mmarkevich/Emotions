from django.urls import path
from . import views
from .views import VideoInformationSerializerView, DataAboutUserAndVideoSerializerView



urlpatterns = [
path('test2', VideoInformationSerializerView.as_view()),
path('test3', DataAboutUserAndVideoSerializerView.as_view()),
path('video_list', views.video_list, name='video_list')
]