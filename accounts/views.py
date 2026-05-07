from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistoForm
from django.contrib.auth.models import User

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"]
        )

        if user:
            login(request, user)
            return redirect("index")

        return render(request, "accounts/login.html", {
            "mensagem": "Credenciais inválidas"
        })

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("index")


def registo_view(request):
    form = RegistoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("login")

    return render(request, "accounts/registo.html", {
        "form": form
    })

def magic_link_view(request):

    if request.method == "POST":

        email = request.POST["email"]

        try:
            user = User.objects.get(email=email)

            return redirect('autentica_magic_link', user.id)

        except:
            return render(request, 'accounts/magic_link.html', {
                'mensagem': 'Email não encontrado'
            })

    return render(request, 'accounts/magic_link.html')


def autentica_magic_link_view(request, user_id):

    user = User.objects.get(id=user_id)

    login(request, user)

    return redirect('index')
# Create your views here.
