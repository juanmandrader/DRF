from django.contrib import admin
from .models import Pais, Departamento, Municipio, DivisionTerritorial, Barrio


admin.site.register(Pais)
admin.site.register(Departamento)
admin.site.register(Municipio)
admin.site.register(DivisionTerritorial)
admin.site.register(Barrio)
