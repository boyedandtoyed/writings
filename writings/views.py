from urllib.parse import urlencode

from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . import forms
from . import models

def create_writing(request):
    form = forms.WritingCreationForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        writing = form.save(commit=False)
        writing.main_author = request.user
        writing.save()
        # base_url = reverse_lazy("writings:show_writing")
        # query_string =  urlencode({'slug': writing.slug}) 
        # url = f"{base_url}?{query_string}"
        return redirect("writings:show_writing", slug=writing.slug) 
    return render(request, 'writings/add_writing.html', context={'form':form})

def update_writings(request):
    pass

def delete_writings(request):
    pass


def show_writing(request, slug):
    writing = models.Writing.objects.filter(slug=slug)[0]    
    print(writing)
    return render(request, "writings/writing.html", context={'writing':writing})


def my_writings(request):
    return render(request, 'writings/my_writings.html')