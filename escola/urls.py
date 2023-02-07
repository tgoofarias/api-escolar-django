from django.urls import path
from escola import views


urlpatterns = [
    path("alunos/", views.alunos, name="alunos"),
]