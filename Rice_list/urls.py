from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('Rice_list/',views.Rice_list),
]
