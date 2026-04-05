from django.contrib import admin
from .models import (
    Licenciatura,
    UnidadeCurricular,
    Docente,
    Projeto,
    Tecnologia,
    TFC,
    Competencia,
    Formacao,
    EmpresaParceira,
    MakingOf)



admin.site.register(Licenciatura)
admin.site.register(UnidadeCurricular)
admin.site.register(Docente)
admin.site.register(Projeto)
admin.site.register(Tecnologia)
admin.site.register(TFC)
admin.site.register(Competencia)
admin.site.register(Formacao)
admin.site.register(EmpresaParceira)
admin.site.register(MakingOf)


# Register your models here.
