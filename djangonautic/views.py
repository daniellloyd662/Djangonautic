from django.http import HttpResponse
from django.shortcuts import render

#Each function will be called via path('url', <function name>) in a url.py file
#Render is a function that 'renders' a template. ie passes in variables and returns the resulting html file from template
#request is an object
def homepage(request):
    # return HttpResponse('homepage')     #returns the text homepage
    return render(request, 'homepage.html')
def about(request):
    # return HttpResponse('about')
    return render(request, 'about.html')
