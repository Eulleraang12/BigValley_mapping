# Generated by Django 3.0.7 on 2020-06-19 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BigV_app_map', '0012_auto_20200619_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dados_mapeamento',
            name='Possui_Influência_ou_interesse_militar',
        ),
        migrations.AddField(
            model_name='dados_mapeamento',
            name='possui_Influencia_ou_interesse_militar',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dados_mapeamento',
            name='possui_mercado_Global',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=0),
            preserve_default=False,
        ),
    ]
