from django.shortcuts import render, redirect
from django.contrib.auth import login as djangologin, authenticate,logout as djangoLogout
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from accounts.forms import UserForm
from django.contrib import messages 
from django.contrib.auth.views import (PasswordResetView,
                                       PasswordResetDoneView,
                                       PasswordResetConfirmView,
                                       PasswordResetCompleteView)
from django.conf import settings
import os

class MyPasswordResetView(PasswordResetView):
    template_name = 'accounts/forget_password.html'
    success_url = reverse_lazy('password_reset_done')

class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'

class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/reset_password.html'
    success_url = reverse_lazy('password_reset_complete')    

class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'

def login(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy('index'))
    
    if request.method == 'POST':
        user = authenticate(request=request, username = request.POST.get('username'), password = request.POST.get('password') )
        if user:
            djangologin(request, user)
            return redirect(reverse_lazy('index'))
        else:
              messages.add_message(request, messages.WARNING, 'Username or password incorrect')
              return render(request, 'accounts/login.html')
        
    return render(request, 'accounts/login.html')

def logout(request):
    djangoLogout(request)
    return redirect(reverse_lazy('login'))

def change_password(request):
    return render(request,'accounts/change_password.html')

def forget_password(request):
    return render(request,'accounts/forget_password.html')

def reset_password(request):
    return render(request,'accounts/reset_password.html')

def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('login'))
        else: 
            if list(form.errors.values()[0][0]) == 'Password not same':
                messages.add_message(request, messages.WARNING, 'Password not same')
        
    context = {'form': form}
    return render(request,'accounts/register.html', context=context)


@login_required
def userprofile(request):
    if request.method == 'POST':
        image = request.FILES.get('picture')

        request.user.profile.image = os.path.join('profile',image.name)
        request.user.profile.save()

        with open(f"{os.path.join(settings.MEDIA_ROOT,'profile',image.name)}", 'wb') as f:
            f.write(image.read())

    return render(request,'accounts/user-profile.html')
    