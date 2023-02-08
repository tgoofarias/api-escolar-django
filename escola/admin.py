from django.contrib import admin
from escola.models import Aluno, Curso

# Register your models here.
class AlunoModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Aluno, AlunoModelAdmin)

class CursoModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso',)
    list_per_page = 20

admin.site.register(Curso, CursoModelAdmin)