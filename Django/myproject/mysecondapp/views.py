from django.shortcuts import render, HttpResponse

# Create your views here.
def show_account(request, username):
    return render(request,  "mysecondapp/account.html")