from django.shortcuts import render, redirect
from django.contrib import messages

from writings import models


def landingpage(request):
    return render(request, 'homescreens/landingpage.html')
    

def home(request):
    if request.user.is_authenticated:
            return render(request, 'homescreens/home.html', context={
                'writings':reversed(models.Writing.objects.all())
            })
    else:
        messages.info(request, 'Sorry, you must log in to access this page')
        return redirect("userprofile:login")
