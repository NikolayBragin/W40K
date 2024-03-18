from django.shortcuts import render, redirect
from . import forms
from .models import Articles, Video, Photo


def index(request):
    news = Articles.objects.order_by('-date')[:3]
    video = Video.objects.order_by('-date')[:6]
    photo = Photo.objects.order_by('-date')[:6]
    context = {'news': news, 'video': video, 'photo': photo}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')

def news(request):
    news = Articles.objects.order_by('-date')
    context = {'news': news}
    return render(request, 'news.html', context)

def video(request):
    video = Video.objects.order_by('-date')
    context = {'video': video}
    return render(request, 'video.html', context)

def photo(request):
    photo = Photo.objects.order_by('-date')
    context = {'photo': photo}
    return render(request, 'photo.html', context)

def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = forms.RegisterForm(request.POST)
    context = {'form': form}
    return render(request, 'registration/register.html', context)
