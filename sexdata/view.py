from django.http import HttpResponse
from django.shortcuts import render

####################################
contexts = {}
contexts['hello'] = 'Hello SexData!'
contexts['qb'] = '桥本有菜'
contexts['sa'] = '山岸逢花'
####################################

def hello(request):
    # return HttpResponse("hello sexdata")
    return render(request, 'index.html', contexts)
def qb(request):
    # return HttpResponse("hello sexdata")
    return render(request, 'qb.html', contexts)
def sa(request):
    # return HttpResponse("hello sexdata")
    return render(request, 'sa.html', contexts)
def signup(request):
    return HttpResponse("signup")
def signin(request):
    return HttpResponse("signin")
