# Generated by Django 3.0.7 on 2020-06-20 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BigV_app_map', '0019_auto_20200620_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dados_mapeamento',
            name='setor_de_atuacao',
            field=models.BooleanField(blank=True, choices=[('industria', 'Indústria'), ('comercio', 'Comércio'), ('servico', 'Serviços')], default=0),
        ),
    ]
