from django.shortcuts import render,HttpResponse

# Create your views here.
def page(request):
    return HttpResponse("<h1>Hello World I am Tawhid from Bangladesh</h1>")

