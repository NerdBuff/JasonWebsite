from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def list_books(request):
    return HttpResponse(request.user.username)
    #return HttpResponse("We can put anything here") #This puts a simple HTML text in the page
