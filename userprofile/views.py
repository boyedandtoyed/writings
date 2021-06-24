from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import CustomUserCreationForm

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'userprofile/profile.html')
    else:
        messages.info(request, 'Sorry, you must log in to access this page')
        return redirect("userprofile:login")

    
def login_view(request):
    if request.user.is_authenticated:
        return redirect("userprofile:profile")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("userprofile:profile")
        else:
            messages.info(request, "Either your username or password is invalid, please enter them correctly")
    return render(request, "userprofile/login.html")


def logout_view(request):
    logout(request)
    return redirect('userprofile:login')

def register_view(request):
    if request.user.is_authenticated:
        return redirect("userprofile:profile")
    form = CustomUserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Account was created successfully, but please verify your email before logging in.')
        return redirect('userprofile:login')
    context = {'form': form}
    return render(request, "userprofile/register.html", context)
    
