from django.shortcuts import render


# СТРАНИЦЫ СОЗДАННЫЕ ПРИ ИЗУЧЕНИИ DJANGO
# def index(request):
#     return render(request, 'main/index.html')
#
#
# def about(request):
#     return render(request, 'main/about.html')
#
#
# def instruction(request):
#     return render(request, 'main/instruction.html')

# РЕГИСТРАЦИЯ И ВХОД В СИСТЕМУ
def login(request):
    return render(request, 'main/login.html')

# ТЕСТОВЫЙ РЕГИСТРАЦИОННЫЙ ШАБЛОН
def registration(request):
    return render(request, 'main/registration.html')

#ТЕСТОВЫЙ ВХОД В СИСТЕМУ
def enter(request):
    return render(request, 'main/enter.html')

# ВИДЕО
def video_link(request):
    return render(request, 'main/video_link.html')


def video_list(request):
    return render(request, 'main/video_list.html')


def video(request):
    return render(request, 'main/video.html')

