from django.shortcuts import render, HttpResponse

# Create your views here.
def home_page(request):
    return render(request, "myfirstapp/home.html")

def aboutus_page(request):
    return render(request, "myfirstapp/aboutus.html")

def products_page(request):
    return render(request, "myfirstapp/products.html")