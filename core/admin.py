from django.contrib import admin
from core.models import Evento

# Register your models here.

class EventosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'date_evento', 'data_criacao')
    list_filter = ('usuario',)


admin.site.register(Evento, EventosAdmin)