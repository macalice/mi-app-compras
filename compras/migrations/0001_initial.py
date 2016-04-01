# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('fechaRegistro', models.DateTimeField(default=django.utils.timezone.now)),
                ('fechaCompra', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
