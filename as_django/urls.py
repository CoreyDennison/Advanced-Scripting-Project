from django.urls import path
from . import views

urlpatterns = [
    path("", views.student_attend_view, name="home"),
]