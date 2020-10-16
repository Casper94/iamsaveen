from django.contrib import admin
from . import models, views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import (
    BlogHomeView,
    PostCommentView,
    AddBlogPostView,
    UpdateBlogPostView,
    DeletePostView,
    # AddCategoryView,
)

urlpatterns = [
    path('', views.index, name = "index"),
    path('about/', views.about, name = 'about'),
    path('resume/', views.resume, name = 'resume'),
    path('skills/', views.skills, name = 'skills'),
    path('services/', views.services, name = 'services'),
    path('projects/', views.projects, name = 'projects'),
    path('contactMe/', views.contact_me, name = 'contact_me'),
    path('blog/', BlogHomeView.as_view(), name ='blog'),
    path('posts/<int:pk>', PostCommentView.as_view(), name='blogpost-detail'),
    path('add_post/', AddBlogPostView.as_view(), name='add_post'),
    # path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path ('posts/edit/<int:pk>', UpdateBlogPostView.as_view (), name='blogpost-update'),
    path ('posts/<int:pk>/delete', DeletePostView.as_view (), name='blogpost-delete'),
    # path ('category/<str:cats>/', views.categoryView, name='categories'),

]

urlpatterns += staticfiles_urlpatterns()