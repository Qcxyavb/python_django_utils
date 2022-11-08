from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello world~")

def page1(request):
    context={}
    context['t1']='hello world~'
    return render(request,'p1.html',context)

def page2(request):
    views_name = "text2"
    return render(request,'p1.html',{"name":views_name})