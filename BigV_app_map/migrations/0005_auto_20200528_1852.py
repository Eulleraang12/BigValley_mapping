# Generated by Django 3.0.5 on 2020-05-28 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BigV_app_map', '0004_auto_20200528_1847'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dados_Cadastrais',
            new_name='Dados_Mapeamento',
        ),
        migrations.AlterModelOptions(
            name='dados_mapeamento',
            options={'verbose_name_plural': 'Dados_Mapeamento'},
        ),
    ]
