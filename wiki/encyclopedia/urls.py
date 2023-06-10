from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.content, name="title"),
    path("search", views.search, name="search"),
    path("newpage", views.newpage, name="newpage"),
    path("wiki/<str:title>/edit", views.edit, name="edit"),
    path("random", views.random_entry, name="random"),
    

    
]
