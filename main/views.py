from django.shortcuts import render
from rest_framework import generics
from .models import User, VideoInformation, DataAboutUserAndVideo
from.sterializers import UserSerializer, VideoInformationSerializer, DataAboutUserAndVideoSerializer


class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class VideoInformationSerializerView(generics.CreateAPIView):
    queryset = VideoInformation.objects.all()
    serializer_class = VideoInformationSerializer


class DataAboutUserAndVideoSerializerView(generics.CreateAPIView):
    queryset = DataAboutUserAndVideo.objects.all()
    serializer_class = DataAboutUserAndVideoSerializer


# СТРАНИЦЫ СОЗДАННЫЕ ПРИ ИЗУЧЕНИИ DJANGO
def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def instruction(request):
    return render(request, 'main/instruction.html')

# РЕГИСТРАЦИЯ И ВХОД В СИСТЕМУ
def login(request):
    return render(request, 'main/login.html')


def registration(request):
    return render(request, 'main/registration.html')


def enter(request):
    return render(request, 'main/enter.html')

# ВИДЕО
def video_link(request):
    return render(request, 'main/video_link.html')


def video(request):
    return render(request, 'main/video.html')
