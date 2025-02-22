from django.shortcuts import render, HttpResponse

# Create your views here.
def show_account(request, username):
    return render(request,  "mysecondapp/account.html", context={'username':username})

def show_accounts(request):
    all_users = [
        {
        "username" : "Test username 1", 
        "Name" : "Test name 1",
        "Age" : "22",
        "Email" : "Testemail1@gmail.com"
        },
        {
        "username" : "Test username 2", 
        "Name" : "Test name 2",
        "Age" : "23",
        "Email" : "Testemail2@gmail.com"
        },
        {
        "username" : "Test username 3", 
        "Name" : "Test name 3",
        "Age" : "24",
        "Email" : "Testemail3@gmail.com"
        },
    ]
    return render(request, "mysecondapp/accounts.html", context={'all_users':all_users})