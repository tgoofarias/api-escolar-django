from django.urls import path, include
from escola import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', views.AlunosViewSet, basename='Alunos')
router.register('cursos', views.CursosViewSet, basename='Cursos')
router.register('matriculas', views.MatriculasViewSet, basename='Matriculas')

urlpatterns = [
    path('', include(router.urls)),
]