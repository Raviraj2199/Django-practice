from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def student(request):
    return HttpResponse('<h1>Welcome Students Field</h1><br></br>')
