from django.urls import path
from . import views
from .views import UserView, VideoInformationSerializerView, DataAboutUserAndVideoSerializerView


urlpatterns = [
path('test', UserView.as_view()),
path('test2', VideoInformationSerializerView.as_view()),
path('test3', DataAboutUserAndVideoSerializerView.as_view()),
path ('registration', views.registration, name='registration'),
]