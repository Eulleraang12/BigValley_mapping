# Generated by Django 3.0.7 on 2020-06-20 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BigV_app_map', '0046_auto_20200620_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dados_mapeamento',
            name='possui_mercado_Global',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=3),
        ),
    ]
