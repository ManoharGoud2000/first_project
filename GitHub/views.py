from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def GitHub(request):
    return HttpResponse('<marquee><h1>GitHub is running Succesfully</h1></marquee>')
def Pro(request):
    return HttpResponse('<marquee><h1>Waiting .......</h1></marquee>')
