from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def alunos(request):
    if request.method == 'GET':
        alunos = {
            'id': 1,
            'nome': 'Tiago Farias Barbosa'
        }
        return JsonResponse(alunos)