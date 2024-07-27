from django.urls import path
from . import views

urlpatterns = [
    path('members/',views.member,name='members'),
    path("members/details/<int:id>",views.details,name="details"),
]