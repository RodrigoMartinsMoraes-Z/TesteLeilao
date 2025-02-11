from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator

from core.forms import LeiloeiroCreationForm, MatriculaForm, UserRegistrationForm

from .models import Anexo, Leiloeiro, Matricula

@login_required
def home_view(request):
    try:
        leiloeiro = request.user.leiloeiro
    except Leiloeiro.DoesNotExist:
        return redirect('perfil')

    if request.method == 'POST':
        matricula_form = MatriculaForm(request.POST)
        if matricula_form.is_valid():
            matricula = matricula_form.save(commit=False)
            matricula.leiloeiro = leiloeiro
            matricula.save()
            return redirect('home')
    else:
        matricula_form = MatriculaForm()

    matriculas = Matricula.objects.filter(leiloeiro=leiloeiro)
    anexos_list = Anexo.objects.filter(leiloeiro=leiloeiro).order_by('-id')
    paginator = Paginator(anexos_list, 5)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'core/home.html', {
        'page_obj': page_obj,
        'matricula_form': matricula_form,
        'matriculas': matriculas,
    })

@login_required
def perfil_view(request):
    if request.method == 'POST':
        form = LeiloeiroCreationForm(request.POST)
        if form.is_valid():
            leiloeiro = form.save(commit=False)
            leiloeiro.user = request.user
            leiloeiro.save()
            return redirect('home')
    else:
        form = LeiloeiroCreationForm()
    return render(request, 'core/perfil.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        leiloeiro_form = LeiloeiroCreationForm(request.POST)

        if user_form.is_valid() and leiloeiro_form.is_valid():
            user = user_form.save()
            leiloeiro = leiloeiro_form.save(commit=False)
            leiloeiro.user = user
            leiloeiro.save()
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
        leiloeiro_form = LeiloeiroCreationForm()
    
    return render(request, 'core/register.html', {
        'user_form': user_form,
        'leiloeiro_form': leiloeiro_form
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'core/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

