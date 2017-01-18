# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caixa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('historico', models.TextField(default=b'', null=True, blank=True)),
                ('categoria', models.CharField(max_length=15)),
                ('valor', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('historico', models.TextField(default=b'', null=True, blank=True)),
                ('valor', models.DecimalField(max_digits=10, decimal_places=2)),
                ('valor_pago', models.DecimalField(max_digits=10, decimal_places=2)),
                ('categoria', models.CharField(max_length=15)),
                ('criacao_at', models.DateField(auto_now_add=True)),
                ('pagamento_at', models.DateField(null=True, blank=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PlanoConta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(default=None, null=True, blank=True)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='conta',
            name='plano_conta',
            field=models.ForeignKey(to='livro_caixa.PlanoConta'),
        ),
    ]
