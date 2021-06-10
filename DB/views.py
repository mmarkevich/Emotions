from django.shortcuts import render, redirect
from rest_framework import generics
from .models import DB_VideoInformation, DataAboutUserAndVideo
from DB.sterializers import VideoInformationSerializer, DataAboutUserAndVideoSerializer
from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from streamapp.camera import VideoCamera
import time


class VideoInformationSerializerView(generics.ListAPIView):
    queryset = DB_VideoInformation.objects.all()
    serializer_class = VideoInformationSerializer


class DataAboutUserAndVideoSerializerView(generics.CreateAPIView):
    queryset = DataAboutUserAndVideo.objects.all()
    serializer_class = DataAboutUserAndVideoSerializer



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
    link = DB_VideoInformation.objects.all()

    return render(request, 'DB/video_list.html', {'link': link})
