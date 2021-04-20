from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:ent>", views.show_entry, name="show_entry"),
]