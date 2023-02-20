from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def legday(request):
    return HttpResponse('<h1>today is legday</h1><br></br><h2>dont break a leg</h2>')

def cardio(request):
    return HttpResponse('<h1>today is cardio</h1><br></br><h2>one step at a time</h2>')

