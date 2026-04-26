from django.urls import path
from . import views

urlpatterns = [

    #Página principal

    path('', views.index_view, name='index'),

    

    path('projeto/', views.projeto_view, name="projeto"),
    path('tecnologia/', views.tecnologia_view, name="tecnologia"), 
    path('competencia/', views.competencia_view, name="competencia"),
    path('formacao/', views.formacao_view, name="formacao"),

    path('projeto/<int:projeto_id>/edita', views.edita_projeto_view,name="edita_projeto"),
    path('tecnologia/<int:tecnologia_id>/edita', views.edita_tecnologia_view,name="edita_tecnologia"),
    path('competencia/<int:competencia_id>/edita', views.edita_competencia_view,name="edita_competencia"),
    path('formacao/<int:formacao_id>/edita', views.edita_formacao_view,name="edita_formacao"), 

    path('projeto/<int:projeto_id>/apaga', views.apaga_projeto_view,name="apaga_projeto"),
    path('tecnologia/<int:tecnologia_id>/apaga', views.apaga_tecnologia_view,name="apaga_tecnologia"),
    path('competencia/<int:competencia_id>/apaga', views.apaga_competencia_view,name="apaga_competencia"),
    path('formacao/<int:formacao_id>/apaga', views.apaga_formacao_view,name="apaga_formacao"),



    path('projetos/', views.pagina_projetos_view, name='pagina_projetos'),
    path('projeto/<int:projeto_id>/', views.pagina_projeto_view, name='pagina_projeto'),
    path('tecnologias/', views.pagina_tecnologias_view, name='pagina_tecnologias'),
    path('tecnologia/<int:tecnologia_id>/', views.pagina_tecnologia_view, name='pagina_tecnologia'),
    path('competencias/', views.pagina_competencias_view, name='pagina_competencias'),
    path('competencia/<int:competencia_id>/', views.pagina_competencia_view, name='pagina_competencia'),

    path('formacoes/', views.pagina_formacoes_view, name='pagina_formacoes'),
    path('formacao/<int:formacao_id>/', views.pagina_formacao_view, name='pagina_formacao'),


    
]