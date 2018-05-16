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
    return HttpResponse("signup")
def signin(request):
    return HttpResponse("signin")
def actress(request):
    return HttpResponse("actress")
def firm(request):
    return HttpResponse("firm")
def sort(request):
    return HttpResponse("sort")
def sale(request):
    return HttpResponse("sale")
def rank(request):
    return HttpResponse("rank")
def api(request):
    return HttpResponse("api")

