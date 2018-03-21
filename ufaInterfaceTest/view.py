# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello python django.")

def hello1(request):
    context = {}
    context['hello1'] = 'Hello Django!'
    return render(request,'home.html',context)