from django.shortcuts import render, redirect
from BigV_app_map.models import Dados_Mapeamento,Endereco
from BigV_app_map.forms import TransacaoForm
# import datetime 

# Create your views here.

def home(request):
    
    return  render(request, 'env_BigV/home.html')


def sobre_map(request):
    
    return  render(request, 'env_BigV/sobre_map.html')

def vertentes_map(request):
    
    return  render(request, 'env_BigV/vertentes_map.html')


def formulario(request):
    data = {}
    form = TransacaoForm()

    # data['dados'] = Dados_Mapeamento.objects.all()
    return  render(request, 'env_BigV/formulario.html', data)


def validacao_form(request):
    data = {}
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("url_home")
    
    data['form'] = form
    return render(request, 'env_BigV/formulario.html', data)

