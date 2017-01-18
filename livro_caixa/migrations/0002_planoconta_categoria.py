# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro_caixa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='planoconta',
            name='categoria',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
    ]
