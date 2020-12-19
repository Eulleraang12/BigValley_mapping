from django.shortcuts import render, redirect
from BigV_app_map.models import Dados_Mapeamento_startup
from BigV_app_map.forms import TransacaoForm_Dados_startup,TransacaoForm_Dados_empresa


# Create your views here.

def home(request):
    
    return  render(request, 'BigV_app_map/home.html')

def startup(request):
    data = {}

    form_dados = TransacaoForm_Dados_startup(request.POST or None)

    if form_dados.is_valid(): 
        form_dados.save()
        return redirect('/')

    data['Dados'] = form_dados
    return render(request, 'BigV_app_map/startup_form.html', data)

def empresa(request):
    data = {}

    form_dados = TransacaoForm_Dados_empresa(request.POST or None)

    if form_dados.is_valid(): 
        form_dados.save()
        return redirect('/')

    data['Dados2'] = form_dados
    return render(request, 'BigV_app_map/empresa_form.html', data)


