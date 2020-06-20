# Generated by Django 3.0.7 on 2020-06-20 22:43

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('BigV_app_map', '0043_auto_20200620_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dados_mapeamento',
            name='possui_Influencia_ou_interesse_militar',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=3),
        ),
        migrations.AlterField(
            model_name='dados_mapeamento',
            name='possui_mercado_Global',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=3),
        ),
        migrations.AlterField(
            model_name='dados_mapeamento',
            name='segmento_area',
            field=models.CharField(choices=[['Aer', 'Aeronáutico/Aeroespacial'], ['Agr', 'Agronégocio'], ['Arq', 'Arquitetura e Designer'], [' Ar', ' Arte e Cultura'], ['Aut', 'Automotivo'], ['Bel', 'Beleza'], ['Bio', 'Biotecnologia'], ['Com', 'Comida e Bebida'], ['Con', 'Construção Civil'], ['Edu', 'Educação'], ['Far', 'Farmacêutico'], ['Ges', 'Gestão de Resíduos'], ['Mat', 'Materias primas e químicos'], ['Mod', 'Moda e Têxtil'], ['Míd', 'Mídia'], ['Saú', 'Saúde'], ['Ser', 'Serviço'], ['Tec', 'Tech: TI e Software'], ['Tec', 'Tech: Hardware e Equipamentos'], ['Tec', 'Tech: Mobile'], ['Tur', 'Turismo'], ['Tel', 'Telecomunicações'], ['Var', 'Varejo'], ['Naú', 'Naútico'], ['Nav', 'Naval'], ['Emp', 'Empresas/Negócios (Business to Business)'], ['Con', 'Consumidores (Business to Consumer)'], ['Gov', 'Governo']], default=3, max_length=3),
        ),
        migrations.AlterField(
            model_name='dados_mapeamento',
            name='segmento_de_atuacao',
            field=models.CharField(choices=[['Aer', 'Aeronáutico'], ['Agr', 'Agronégocio'], ['Arq', 'Arquitetura e Design'], ['Aut', 'Automotivo'], ['Bel', 'Beleza'], ['Bio', 'Biotecnologia'], ['Com', 'Comida e Bebida'], ['Con', 'Construção Civil'], ['Edu', 'Educação'], ['Far', 'Farmacêutico'], ['Ges', 'Gestão de Resíduos'], ['Mat', 'Matérias Primas e Químicos'], ['Mod', 'Moda e Textil'], ['Mid', 'Midia'], ['Saú', 'Saúde e Bem-estar'], ['Ser', 'Serviço'], ['Tec', 'Tech: TI e Software'], ['Tec', 'Tech: Hardware e Equipamentos'], ['Tec', 'Tech: Mobile'], ['Tel', 'Telecomunicações'], ['Var', 'Varejo'], ['Naú', 'Naútico'], ['Nav', 'Naval'], ['Art', 'Arte e Cultura'], ['Tur', 'Turismo']], default=3, max_length=3),
        ),
        migrations.AlterField(
            model_name='dados_mapeamento',
            name='setor_de_atuacao',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('ind', 'Indústria'), ('com', 'Comércio'), ('ser', 'Serviços')], max_length=11),
        ),
        migrations.AlterField(
            model_name='dados_mapeamento',
            name='tipo_de_cliente',
            field=models.CharField(choices=[('B2B', 'Empresas e Negócios (B2B) '), ('B2C', 'Consumidores (B2C) '), ('GOV', 'Governo')], default=3, max_length=3),
        ),
    ]