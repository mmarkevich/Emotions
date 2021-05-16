from rest_framework import serializers
from .models import User
from .models import VideoInformation
from .models import DataAboutUserAndVideo


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'nickname', 'password', 'male', 'female', 'age')


class VideoInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoInformation
        fields = ('id', 'link')


class DataAboutUserAndVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataAboutUserAndVideo
        fields = ('id', 'ID_user', 'ID_video_information', 'ID_screenshot', 'second',
                  'neutral', 'disgust', 'sad', 'happy', 'fear', 'disgust', 'angry', 'dominant_emotion', 'edited_dominant_emotion')
