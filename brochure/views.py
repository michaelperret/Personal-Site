from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

def home(request):
    return render_to_response("base.html")

def hello(request,name,color):
    name = name.lower()
    return render_to_response("base.html",
                              {'name': name,
                                'color': color
                              }
            )


def aboutme(request):
    return render_to_response("aboutme.html")

def projects(request):
    return render_to_response("projects.html")

def contact(request):
    return render_to_response("contact.html")

def professional(request):
    return render_to_response("professional.html")

def fizzbuzz(request,num1,num2):
    res = ''
    if int(num1) % 3 == 0:
        res+='fizz'
    if int(num2) % 5 == 0:
        res+='buzz'
    return HttpResponse("<h1 style='font-family:sans-serif'>"+res+"</h1>")



def name(request):
    return HttpResponse("Hi,\nMy name is Michael! Welcome to my page!")


# Create your views here.
