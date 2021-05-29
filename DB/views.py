from django.shortcuts import render, redirect
from rest_framework import generics
from .models import User, VideoInformation, DataAboutUserAndVideo
from DB.sterializers import UserSerializer, VideoInformationSerializer, DataAboutUserAndVideoSerializer
from .forms import UserForm


class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class VideoInformationSerializerView(generics.CreateAPIView):
    queryset = VideoInformation.objects.all()
    serializer_class = VideoInformationSerializer


class DataAboutUserAndVideoSerializerView(generics.CreateAPIView):
    queryset = DataAboutUserAndVideo.objects.all()
    serializer_class = DataAboutUserAndVideoSerializer


def registration(request):
    error = ''
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('video_link')
        else:
            error = 'Не правильно введена форма'

    form = UserForm()

    data = {
        'form': form
    }

    return render(request, 'DB/registration.html', data)