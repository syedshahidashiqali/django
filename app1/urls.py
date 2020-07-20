from . import views
from django.urls import path

urlpatterns = [
    path("", views.fun1, name="fun1"),
    path("<str:name>", views.greet, name="greet"),
    path("fun2", views.fun2, name="fun2"),
    path("fun3", views.fun3, name="fun3"),
    path("fun4", views.fun4, name="fun4"),
]