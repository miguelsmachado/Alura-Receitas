from django.contrib import admin
from .models import Receitas


class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'publicada')
    list_display_links = ('id', 'nome_receita')
    list_editable = ('publicada',)
    list_filter = ('categoria',)
    list_per_page = 10
    search_fields = ('nome_receita',)


admin.site.register(Receitas, ReceitaAdmin)
