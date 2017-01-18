# -*- encoding: utf-8 -*-

from django.db import models

# Create your models here.

CATEGORIA_CHOICES = (
    ('Pagamento', 'Pagamento'),
    ('Recebimento', 'Recebimento'),
)

class PlanoConta(models.Model):
    '''
    Classe Plano Contas que abstrai a classificação das contas de pagamento e recebimento
    '''
    nome = models.CharField(max_length=100)
    descricao = models.TextField(default=None, null=True, blank=True)
    create_at = models.DateField(auto_now_add=True)
    categoria = models.CharField(max_length=15, null=True, blank=True, choices=CATEGORIA_CHOICES, default='')
    status = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.nome
    
    def get_status_view(self):
        show = None
        if self.status:
            show = 'Ativa'
        else:
            show = 'Bloqueada'
            
        return show

class Conta(models.Model):
    '''
    Classe que abstrai as contas de pagamentos e recebimentos.
    '''
    plano_conta = models.ForeignKey(PlanoConta)
    historico = models.TextField(default='', blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=15)
    criacao_at = models.DateField(auto_now_add=True)
    pagamento_at = models.DateField(blank=True, null=True)
    status = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.historico
    
class Caixa(models.Model):
    '''
    Classe que abstrai as lançamentos diários de pagamantos e recebimentos.
    '''
    historico = models.TextField(default='', blank=True, null=True)
    categoria = models.CharField(max_length=15)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __unicode__(self):
        return self.historico