from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('news', views.news, name='news'),
    path('video', views.video, name='video'),
    path('photo', views.photo, name='photo'),
    path('allrights', views.allrights, name='allrights'),
    path('feedback', views.feedback, name='feedback'),
    path('marketing', views.marketing, name='marketing'),
    path('support', views.support, name='support'),
    path('links', views.links, name='links'),
    path('something', views.something, name='something'),
    path('google84caa8db29903f31', views.google84caa8db29903f31, name='google84caa8db29903f31'),

]


