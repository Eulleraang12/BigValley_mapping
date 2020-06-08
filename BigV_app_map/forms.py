from django.forms import ModelForm
from BigV_app_map.models import *

class TransacaoForm(ModelForm):
    class Meta:
        model = Dados_Mapeamento
        fields = [ 'nome','cnpj','site','email'] 
