from django.urls import path
from . import views

urlpatterns = [
    path('artigos/', views.artigos_view, name='artigos'),
    path('artigo/<int:artigo_id>/', views.artigo_view, name='artigo'),
    path('artigo/novo/', views.novo_artigo_view, name='novo_artigo'),
    path('artigo/<int:artigo_id>/edita/', views.edita_artigo_view, name='edita_artigo'),
    path('artigo/<int:artigo_id>/like/', views.like_artigo_view, name='like_artigo'),
]