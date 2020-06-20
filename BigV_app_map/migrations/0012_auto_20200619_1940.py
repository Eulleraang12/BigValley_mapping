# Generated by Django 3.0.7 on 2020-06-19 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BigV_app_map', '0011_dados_mapeamento_tipo_de_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='dados_mapeamento',
            name='Possui_Influência_ou_interesse_militar',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')],default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dados_mapeamento',
            name='possui_mercado_Global',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')],default=0),
            preserve_default=False,
        ),
    ]
