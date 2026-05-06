from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistoForm

from .forms import ProjetoForm
from .forms import TecnologiaForm
from .forms import CompetenciaForm
from .forms import FormacaoForm

from .models import Projeto
from .models import Tecnologia
from .models import Competencia
from .models import Formacao
from .models import MakingOf

#Página principal
def is_gestor_portfolio(user):
    return user.is_authenticated and (user.is_superuser or user.groups.filter(name="gestor-portfolio").exists())

def index_view(request):
    projetos = Projeto.objects.all()
    context = {
        'projetos': projetos,
    }

    return render(request, 'portfolio/index.html', context)

#Sobre esta aplicação

def sobre_view(request):
    tecnologias = Tecnologia.objects.filter(nome__in=[
        'Django', 'Python', 'HTML', 'Git',
    ])

    makingofs = MakingOf.objects.all()

    context = {
        'tecnologias': tecnologias,
        'makingofs': makingofs,
    }

    return render(request, 'portfolio/sobre.html', context)










def pagina_projetos_view(request):
    projetos = Projeto.objects.all()
    return render(request, 'portfolio/pagina_projetos.html', {'projetos': projetos,'gestor': is_gestor_portfolio(request.user)})

def pagina_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    return render(request, 'portfolio/pagina_projeto.html', {'projeto': projeto, 'gestor': is_gestor_portfolio(request.user)})

def pagina_tecnologias_view(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/pagina_tecnologias.html', {'tecnologias': tecnologias, 'gestor': is_gestor_portfolio(request.user)})

def pagina_tecnologia_view(request, tecnologia_id):
    tecnologia = Tecnologia.objects.get(id=tecnologia_id)
    return render(request, 'portfolio/pagina_tecnologia.html', {'tecnologia': tecnologia, 'gestor': is_gestor_portfolio(request.user)})

def pagina_competencias_view(request):
    competencias = Competencia.objects.all()
    return render(request, 'portfolio/pagina_competencias.html', {'competencias': competencias, 'gestor': is_gestor_portfolio(request.user)})

def pagina_competencia_view(request, competencia_id):
    competencia = Competencia.objects.get(id=competencia_id)
    return render(request, 'portfolio/pagina_competencia.html', {'competencia': competencia,  'gestor': is_gestor_portfolio(request.user)})

def pagina_formacoes_view(request):
    formacoes = Formacao.objects.all()
    return render(request, 'portfolio/pagina_formacoes.html', {'formacoes': formacoes, 'gestor': is_gestor_portfolio(request.user)})

def pagina_formacao_view(request, formacao_id):
    formacao = Formacao.objects.get(id=formacao_id)
    return render(request, 'portfolio/pagina_formacao.html', {'formacao': formacao,  'gestor': is_gestor_portfolio(request.user)})



@login_required
def projeto_view(request):

    form = ProjetoForm(request.POST or None, request.FILES) 
    
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {'form': form}
    return render(request, 'portfolio/projeto.html', context)

@login_required
def tecnologia_view(request):
    form = TecnologiaForm(request.POST or None, request.FILES) 
    
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {'form': form}
    return render(request, 'portfolio/tecnologia.html', context)

@login_required
def competencia_view(request):
    form = CompetenciaForm(request.POST or None, request.FILES) 
    
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {'form': form}
    return render(request, 'portfolio/competencia.html', context)

@login_required
def formacao_view(request):
    form = FormacaoForm(request.POST or None, request.FILES) 
    
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {'form': form}
    return render(request, 'portfolio/formacao.html', context)



@login_required
def edita_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    
    if request.POST:
        form = ProjetoForm(request.POST or None, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form = ProjetoForm(instance=projeto) 
        
    context = {'form': form, 'projeto':projeto}
    return render(request, 'portfolio/edita_projeto.html', context)

@login_required
def edita_tecnologia_view(request, tecnologia_id):
    tecnologia = Tecnologia.objects.get(id=tecnologia_id)
    
    if request.POST:
        form = TecnologiaForm(request.POST or None, request.FILES, instance=tecnologia)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TecnologiaForm(instance=tecnologia) 
        
    context = {'form': form, 'tecnologia':tecnologia}
    return render(request, 'portfolio/edita_tecnologia.html', context)

@login_required
def edita_competencia_view(request, competencia_id):
    competencia = Competencia.objects.get(id=competencia_id)
    
    if request.POST:
        form = CompetenciaForm(request.POST or None, request.FILES, instance=competencia)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CompetenciaForm(instance=competencia) 
        
    context = {'form': form, 'competencia':competencia}
    return render(request, 'portfolio/edita_competencia.html', context)

@login_required
def edita_formacao_view(request, formacao_id):
    formacao = Formacao.objects.get(id=formacao_id)
    
    if request.POST:
        form = FormacaoForm(request.POST or None, request.FILES, instance=formacao)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FormacaoForm(instance=formacao) 
        
    context = {'form': form, 'formacao':formacao}
    return render(request, 'portfolio/edita_formacao.html', context)



@login_required
def apaga_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    projeto.delete()
    return redirect('index')

@login_required
def apaga_tecnologia_view(request, tecnologia_id):
    tecnologia = Tecnologia.objects.get(id=tecnologia_id)
    tecnologia.delete()
    return redirect('tecnologias')

@login_required
def apaga_competencia_view(request, competencia_id):
    competencia = Competencia.objects.get(id=competencia_id)
    competencia.delete()
    return redirect('competencias')

@login_required
def apaga_formacao_view(request, formacao_id):
    formacao = Formacao.objects.get(id=formacao_id)
    formacao.delete()
    return redirect('formacoes')












# Create your views here.
