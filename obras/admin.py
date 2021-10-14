from django.contrib import admin

from obras.models import Obras, Autor


class ObrasAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'editora', 'foto')


class AutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')


admin.site.register(Obras, ObrasAdmin)
admin.site.register(Autor, AutorAdmin)
