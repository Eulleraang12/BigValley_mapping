# Generated by Django 3.0.7 on 2020-06-20 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BigV_app_map', '0050_dados_mapeamento_startup_foi_fundada_dentro_dos_5_anos_de_graduacao_dos_fundadores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dados_mapeamento',
            name='startup_foi_fundada_dentro_dos_5_anos_de_graduacao_dos_fundadores',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=0),
        ),
    ]