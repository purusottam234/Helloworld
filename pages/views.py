from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homePageView(request):
    return HttpResponse("Hello guys welcome to cscteach online django tutorial")