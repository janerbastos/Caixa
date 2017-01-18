# -*- encoding: utf-8 -*-

from django.forms import models
from livro_caixa.models import PlanoConta
from django import forms
from django.core.exceptions import ValidationError

class PlanoContaForm(models.ModelForm):

    class Meta:
        model = PlanoConta
        fields = (
            'categoria', 'nome', 'descricao', 'status'
            )
        labels = {
            'nome' : 'Nome da conta',
            'descricao' : 'Outras informações',
            'categoria' : 'Categoria da conta',
            'status' : 'Plano de conta ativa'
            }
        help_texts = {
            'nome': 'Obrigatório. 30 caracteres ou menos. Somente letras, dígitos e @/./+/-/_.',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder':'Informe'}),
            
            }
    def clean_categoria(self):
        categoria = self.cleaned_data.get('categoria', False)
        if categoria == None:
            raise ValidationError("Categoria é obrigatória")
        return self.cleaned_data.get('categoria', '')
        
        