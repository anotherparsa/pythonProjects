from django.urls import path
from . import views

urlpatterns = [
    path('accounts/', views.show_accounts),
    path('accounts/<username>', views.show_account),
]