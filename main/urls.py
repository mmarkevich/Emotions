from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='home'),
    # path('about', views.about, name='about'),
    # path('instruction',  views.instruction, name='instruction'),
    path('', views.login, name='log_in'),
    path('registration', views.registration, name='registration'),
    path('login/enter', views.enter, name='enter'),
    path('video_link', views.video_link, name='video_link'),
    path('video', views.video, name='video'),
    path('video_list', views.video_list, name='video_list'),
]