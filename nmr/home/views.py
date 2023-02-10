from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('hello iamk  <b>nimesh</b><a href="/about">anchor</a>')
def about(request):
    return HttpResponse('namaste')
