from django.shortcuts import render, HttpResponse
from .models import Account
# Create your views here.
def show_account(request, username):
    return render(request,  "mysecondapp/account.html", context={'username':username})

def show_accounts(request):
    accounts = Account.objects.all()
    return render(request, "mysecondapp/accounts.html", context={'accounts':accounts})