# Generated by Django 3.0.7 on 2020-06-20 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BigV_app_map', '0052_auto_20200620_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dados_mapeamento',
            name='ano_de_fundacao',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='dados_mapeamento',
            name='numero_de_socios',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='dados_mapeamento',
            name='quantas_rodadas',
            field=models.CharField(max_length=10000),
        ),
    ]
