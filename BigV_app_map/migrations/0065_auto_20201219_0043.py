# Generated by Django 3.1.4 on 2020-12-19 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BigV_app_map', '0064_dados_mapeamento_empresa_referente_a_suporte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dados_mapeamento_startup',
            name='email_representante',
            field=models.EmailField(default='+BR', max_length=254),
        ),
    ]
