from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse 

def student_field(request):
    return HttpResponse('<h1>Welcome Students Field</h1><br></br>')


def Hello(request):
    return HttpResponse("<h1>Hello this is hello for Django</h1>")

