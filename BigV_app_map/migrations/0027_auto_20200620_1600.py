# Generated by Django 3.0.7 on 2020-06-20 19:00

from django.db import migrations
import localflavor.br.models


class Migration(migrations.Migration):

    dependencies = [
        ('BigV_app_map', '0026_auto_20200620_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dados_mapeamento',
            name='estado',
            field=localflavor.br.models.BRStateField(default=0, max_length=2),
        ),
    ]
