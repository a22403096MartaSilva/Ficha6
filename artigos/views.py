from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import Artigo
from .forms import ArtigoForm, ComentarioForm

def is_autor(user):
    return user.is_authenticated and user.groups.filter(name='autores').exists()


def artigos_view(request):
    artigos = Artigo.objects.all().order_by('-data_criacao')
    return render(request, 'artigos/artigos.html', {
        'artigos': artigos,
        'autor': is_autor(request.user),
    })


def artigo_view(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)
    form = ComentarioForm()

    if request.method == 'POST' and request.user.is_authenticated:
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.artigo = artigo
            comentario.autor = request.user
            comentario.save()
            return redirect('artigo', artigo.id)

    return render(request, 'artigos/artigo.html', {
        'artigo': artigo,
        'form': form,
        'autor': is_autor(request.user),
    })


@login_required
def novo_artigo_view(request):
    if not is_autor(request.user):
        return redirect('artigos')

    form = ArtigoForm(request.POST or None, request.FILES)

    if form.is_valid():
        artigo = form.save(commit=False)
        artigo.autor = request.user
        artigo.save()
        return redirect('artigos')

    return render(request, 'artigos/novo_artigo.html', {'form': form})


@login_required
def edita_artigo_view(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)

    if artigo.autor != request.user:
        return redirect('artigo', artigo.id)

    form = ArtigoForm(request.POST or None, request.FILES or None, instance=artigo)

    if form.is_valid():
        form.save()
        return redirect('artigo', artigo.id)

    return render(request, 'artigos/edita_artigo.html', {
        'form': form,
        'artigo': artigo,
    })


def like_artigo_view(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)

    if request.user.is_authenticated:
        if request.user in artigo.likes.all():
            artigo.likes.remove(request.user)
        else:
            artigo.likes.add(request.user)

    return redirect('artigo', artigo.id)

# Create your views here.
