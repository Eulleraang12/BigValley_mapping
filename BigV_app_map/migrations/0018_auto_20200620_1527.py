# Generated by Django 3.0.7 on 2020-06-20 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BigV_app_map', '0017_dados_mapeamento_setor_de_atuacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dados_mapeamento',
            name='setor_de_atuacao',
            field=models.CharField(blank=True, choices=[('industria', 'Indústria'), ('comercio', 'Comércio'), ('servico', 'Serviços')], max_length=20),
        ),
    ]
