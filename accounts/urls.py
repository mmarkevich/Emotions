from django.urls import path
from .views import FerLoginView, registration1, FerLogoutView
from DB.views import video_list


urlpatterns = [
path('login', FerLoginView.as_view(), name='login1'),
path('registration1', registration1, name='registration1'),
path('video_list', video_list, name='video_list'),
path('logout', FerLogoutView.as_view(), name='logout1')
    ]