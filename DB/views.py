from django.shortcuts import render, redirect
from rest_framework import generics
from .models import User, VideoInformation, DataAboutUserAndVideo
from DB.sterializers import UserSerializer, VideoInformationSerializer, DataAboutUserAndVideoSerializer
from .forms import UserForm
from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from streamapp.camera import VideoCamera
import time

class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class VideoInformationSerializerView(generics.ListAPIView):
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


def gen(camera):
    sec = 0
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

        predicted_emotion = 'alhamduela'
        time.sleep(1)
        sec += 1

        if sec % 5 == 0 and sec > 4:
            VideoCamera.throwData()

def video_feed(request):
    return StreamingHttpResponse(gen(VideoCamera()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')


def video_list(request):
    link = VideoInformation.objects.all()

    return render(request, 'DB/video_list.html', {'link': link})
