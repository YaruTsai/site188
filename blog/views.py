from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
#    return HttpResponse("Hello, world. You're at the blog index.")
    return render(request, 'blog/index.html') 
