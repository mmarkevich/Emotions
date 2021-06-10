from rest_framework import serializers
from DB.models import  DataAboutUserAndVideo, DB_VideoInformation


class VideoInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DB_VideoInformation
        fields = ('id', 'link')


class DataAboutUserAndVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataAboutUserAndVideo
        fields = ('id', 'ID_user', 'ID_video_information', 'ID_screenshot', 'second',
                  'neutral', 'disgust', 'sad', 'happy', 'fear', 'disgust', 'angry', 'dominant_emotion', 'edited_dominant_emotion')

