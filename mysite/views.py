from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')


def resume(request):
    return render(request,'resume.html')


def skills(request):
    return render(request,'skills.html')


def services(request):
    return render(request,'services.html')


def projects(request):
    return render(request,'projects.html')


def blog(request):
    return render(request,'myblog.html')


def contact_me(request):
    return render(request,'contact_me.html')
