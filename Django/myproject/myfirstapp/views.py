from django.shortcuts import render, HttpResponse

# Create your views here.
def home_page(request):
    return HttpResponse("This is home page")

def aboutus_page(request):
    return HttpResponse("This is about us page")

def products_page(request):
    return HttpResponse("This is products page")