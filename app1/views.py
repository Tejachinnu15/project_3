from django.shortcuts import render
from django.http import HttpResponse
def string1(request):
    return HttpResponse('this my first string')
