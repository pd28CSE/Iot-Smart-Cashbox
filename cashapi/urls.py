from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserDataDisplay.as_view()),
    path('customers/', views.CustomerDataDisplay.as_view()),
]
