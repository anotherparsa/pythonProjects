from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home_page),
    path('aboutus/', views.aboutus_page),
    path('products/', views.products_page),
]
