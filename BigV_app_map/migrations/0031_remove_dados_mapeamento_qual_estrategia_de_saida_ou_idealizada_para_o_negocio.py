# Generated by Django 3.0.7 on 2020-06-20 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BigV_app_map', '0030_auto_20200620_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dados_mapeamento',
            name='qual_estrategia_de_saida_ou_idealizada_para_o_negocio',
        ),
    ]
