from django.shortcuts import render, redirect
from BigV_app_map.models import Dados_Mapeamento, Endereco
from BigV_app_map.forms import TransacaoForm_Dados, TransacaoForm_Endereco


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
    

    form_endereco = TransacaoForm_Endereco(request.POST or None)
    
    if form_dados.is_valid() and form_endereco.is_valid():
        form_dados.save()
        form_endereco.save()
        return redirect("url_home")

    data['Dados'] = form_dados
    data['Endereco'] = form_endereco
    return render(request, 'env_BigV/formulario.html', data)

