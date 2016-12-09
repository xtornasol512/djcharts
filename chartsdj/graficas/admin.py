from django.contrib import admin
# Import Export
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# MOdels
from .models import ExampleSimple, NotasPeriodico, NotasPorEstado

class NotasPeriodicoResource(resources.ModelResource):
    """ Clase necesaria para import export que usa el model NotasPeriodico """
    class Meta:
        model = NotasPeriodico

class NotasPeriodicoAdmin(ImportExportModelAdmin):
    resource_class = NotasPeriodicoResource
    search_fields = ['estado']
    list_display =("id","estado","suma",)

class NotasPorEstadoResource(resources.ModelResource):
    """ Clase necesaria para import export que usa el model NotasPorEstado """
    class Meta:
        model = NotasPorEstado

class NotasPorEstadoAdmin(ImportExportModelAdmin):
    resource_class = NotasPorEstadoResource
    search_fields = ['estado']
    list_display =("id","estado","year","sucesos")
    list_filter = ('estado', 'year',)

admin.site.register(NotasPorEstado, NotasPorEstadoAdmin)
admin.site.register(NotasPeriodico, NotasPeriodicoAdmin)
admin.site.register(ExampleSimple)