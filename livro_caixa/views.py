# -*- encoding: utf-8 -*-

from django.shortcuts import render, redirect
from livro_caixa.models import PlanoConta
from livro_caixa.forms import PlanoContaForm
from django.contrib import messages

# Create your views here.

def index(request):
    template = 'livro_caixa/index.html'
    context = {
        'titulo' : 'Gestor Financeiro'
        }
    return render(request, template, context)

def manage_plano_conta(request, action=None, plano_conta_id=None):
    template = 'livro_caixa/plano_conta.html'
    
    form = None
    
    try:
        plano_conta = PlanoConta.objects.get(id=plano_conta_id)
    except PlanoConta.DoesNotExist:
        plano_conta = PlanoConta()
    
    if action in ('novo', 'editar', 'excluir'):
        
        if action == 'excluir' and plano_conta:
            plano_conta.delete()
            messages.success(request, 'Plano de contas excluido com sucesso',)
            return redirect('plano_conta')
        
        if action == 'novo' and plano_conta_id:
            return redirect('plano_conta', action='novo')
        
        form = PlanoContaForm(request.POST or None, instance=plano_conta)
        if form.is_valid():
            model = form.save(commit=False)
            model.categoria = 'Pagamento'
            model.save()
            messages.success(request, 'Plano de contas salvo com sucesso',)
            return redirect('plano_conta')
        
    plano_contas = PlanoConta.objects.all()
    
    context = {
        'plano_contas' : plano_contas,
        'form' : form,
        'plano_conta' : plano_conta,
        'titulo' : 'Plano de contas',
        }
    return render(request, template, context)