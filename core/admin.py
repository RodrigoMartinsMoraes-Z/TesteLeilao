from django.contrib import admin

from core.utils import enviar_notificacao_anexo
from .models import Leiloeiro, Matricula, Anexo, Estado

admin.site.register(Leiloeiro)
admin.site.register(Matricula)
admin.site.register(Anexo)
admin.site.register(Estado)

class AnexoAdmin(admin.ModelAdmin):
    list_display = ('arquivo', 'leiloeiro', 'matricula')
    search_fields = ('leiloeiro__nome', 'matricula__numero')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        enviar_notificacao_anexo(obj.leiloeiro, obj)