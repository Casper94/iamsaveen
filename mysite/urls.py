from django.contrib import admin
from . import models, views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', views.index, name = "index"),
    path('about', views.about, name = 'about'),
    path('resume', views.resume, name = 'resume'),
    path('skills', views.skills, name = 'skills'),
    path('services', views.services, name = 'services'),
    path('projects', views.projects, name = 'projects'),
    path('contactMe', views.contact_me, name = 'contact_me'),
    path('blog', views.blog, name = 'blog')
]

urlpatterns += staticfiles_urlpatterns()