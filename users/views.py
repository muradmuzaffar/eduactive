from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm, LoginForm
from .models import Profile
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy

from django.contrib.auth.views import PasswordChangeView,PasswordResetDoneView

# Create your views here.


def register(request):
    form = UserCreateForm()

    if request.method == 'POST':
        form = UserCreateForm(request.POST)

        if form.is_valid():
            form.save()
            Profile.objects.create(user = form.save())
            return redirect('log_in')
        else:
            messages.warning(request, 'ERROR!')

    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def log_in(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            print(username, password)

            user = authenticate(request, username=username, password=password)
            print(user)

            if user is not None:
                login(request, user)
                return redirect('landing')
            else:
                messages.info(request, 'email or password is incorrect')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('landing')

class MyPasswordChangeView(PasswordChangeView):
    template_name='password-change.html'
    success_url = reverse_lazy('change_password_complete')


class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name='password-change-done.html'
