# Generated by Django 3.1.4 on 2020-12-16 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BigV_app_map', '0057_auto_20201215_2132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dados_mapeamento_empresa',
            old_name='em_qual_destes_itens_abaixo_seu_cadastro_se_enquadrada',
            new_name='em_qual_destes_itens_abaixo_seu_cadastro_se_enquadra',
        ),
        migrations.AddField(
            model_name='dados_mapeamento_empresa',
            name='em_qual_destes_setores_a_instituicao_se_enquadra',
            field=models.CharField(choices=[('pol', 'Política'), ('cul', 'Cultura'), ('ch', 'Capital Humano'), ('fin', 'Financeiro'), ('sup', 'Suporte'), ('merc', 'Mercado')], default='', max_length=100),
        ),
    ]
