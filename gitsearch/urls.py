from django.urls import path
from .import views

urlpatterns = [
    path('',views.GitSearch,name="git"),
]