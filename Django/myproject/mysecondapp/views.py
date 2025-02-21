from django.shortcuts import render, HttpResponse

# Create your views here.
def show_account(request, username):
    return HttpResponse(f'this is {username} profile page')