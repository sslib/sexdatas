from django.http import HttpResponse
from django.shortcuts import render

#zzzzzz
contexts = {}
contexts['hello'] = 'Hello SexData!'
contexts['qb'] = '桥本有菜'
contexts['sa'] = '山岸逢花'
#zzzzzz

def hello(request):
    return render(request, 'index.html', contexts)
def qb(request):
    return render(request, 'qb.html', contexts)
def sa(request):
    return render(request, 'sa.html', contexts)
def signup(request):
    return HttpResponse("Test：注册页面...")
def signin(request):
    return HttpResponse("Test：登录页面...")
def actress(request):
    return HttpResponse("Test：女忧页面...")
def firm(request):
    return HttpResponse("Test：片商页面...")
def sort(request):
    return HttpResponse("Test：类别页面...")
def sale(request):
    return HttpResponse("Test：优惠页面...")
def rank(request):
    return HttpResponse("Test：排行页面...")
def api(request):
    return HttpResponse("Test：API页面...")

