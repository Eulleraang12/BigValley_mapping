from django.forms import ModelForm
from django import forms
from BigV_app_map.models import Dados_Mapeamento
from django.forms.widgets import TextInput



class TransacaoForm_Dados(ModelForm):
    class Meta:
        model = Dados_Mapeamento
        fields = [ 'nome','site','email',
                  'rua','bairro','cidade',
                   'nome_representante','cargo','email_representante', 
                   ]
                    # 'telefone',,'cnpj''estado', 'cep',
                
                
                               #valodar CNPJ e Email
        widgets = {
            'nome': TextInput(attrs={'placeholder': 'Nome da Startup'}),
            'cnpj': TextInput(attrs={'placeholder': ' xx.xxx.xxx/xxxx-xx'}),
            'site': TextInput(attrs={'placeholder': 'http://www.seuwebsite.com'}),
            'email': TextInput(attrs={'placeholder': 'meuemail@qualquer.com'}),

            'cep': TextInput(attrs={'placeholder': 'xxxxx-xxx'}), ####### fazer Auto preenchimento com CEP
            
            }



    
    
