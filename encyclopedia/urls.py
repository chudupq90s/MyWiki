from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search",views.search, name="search"),
    path("new", views.new, name="new"),
    path("edit", views.edit, name="edit"),
    path("save_edit", views.save_entry, name = "save_edit"),
    path("random", views.random_page, name="random"),
]
