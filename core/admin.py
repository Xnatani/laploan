from django.contrib import admin
from .models import Locatario, Equipamento, Emprestimo


@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'marca', 'modelo', 'status', 'condicao')
    list_filter = ('status', 'condicao', 'marca')
    search_fields = ('codigo', 'numero_serie', 'marca', 'modelo')


@admin.register(Locatario)
class LocatarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'turma', 'telefone')
    list_filter = ('tipo',)
    search_fields = ('nome', 'email', 'telefone')


@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('equipamento', 'locatario', 'data_saida', 'data_prevista', 'data_devolucao', 'esta_atrasado')
    list_filter = ('data_saida', 'data_prevista')
    search_fields = ('equipamento__codigo', 'locatario__nome')
