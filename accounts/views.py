from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from .forms import AuthUserForm
from .forms import UserForm

# views.py
class FerLoginView(LoginView):
    template_name = 'login_page.html'
    form_class = AuthUserForm
    success_url = ('video_list')
    def get_success_url(self):
        return self.success_url


def registration1(request):
    error = ''
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('log_in')
        else:
            error = 'Не правильно введена форма'

    form = UserForm()

    data = {
        'form': form
    }

    return render(request, 'registration_page.html', data)


class FerLogoutView(LogoutView):
    next_page = ('log_in')

