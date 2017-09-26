# coding: utf-8

from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    context = {}
    context['hello'] = 'Hello world!'
    return render(request, 'hello.html', context)

def mainpage(request):
    context = {}
    context['title'] = 'this is a title'
    context['mainpage'] = 'qmlwwylcljchhdl'
    return render(request, 'mainpage.html', context)