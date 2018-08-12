# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('anio', models.PositiveSmallIntegerField()),
                ('orden', models.PositiveIntegerField()),
                ('contenido', models.CharField(max_length=200)),
                ('cant_hojas', models.PositiveSmallIntegerField()),
                ('fecha_digit', models.DateTimeField(blank=True, null=True)),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
