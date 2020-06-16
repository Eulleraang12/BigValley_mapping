from django.shortcuts import render, redirect
from BigV_app_map.models import Dados_Mapeamento
from BigV_app_map.forms import TransacaoForm_Dados


# Create your views here.

def home(request):
    
    return  render(request, 'env_BigV/home.html')


def sobre_map(request):
    
    return  render(request, 'env_BigV/sobre_map.html')

def vertentes_map(request):
    
    return  render(request, 'env_BigV/vertentes_map.html')



def formulario(request):
    data = {}

    form_dados = TransacaoForm_Dados(request.POST or None)

    
    if form_dados.is_valid(): 
        form_dados.save()
        return redirect("url_home")

    data['Dados'] = form_dados
    return render(request, 'env_BigV/formulario.html', data)

