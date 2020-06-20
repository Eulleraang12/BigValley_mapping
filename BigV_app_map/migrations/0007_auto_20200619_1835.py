# Generated by Django 3.0.7 on 2020-06-19 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BigV_app_map', '0006_auto_20200619_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dados_mapeamento',
            name='seg_area',
            field=models.CharField(choices=[['Aer', 'Aeronáutico/Aeroespacial'], ['Agr', 'Agronécio'], ['Arq', 'Arquitetura e Designer'], [' Ar', ' Arte e Cultura'], ['Aut', 'Automotivo'], ['Bel', 'Beleza'], ['Bio', 'Biotecnologia'], ['Com', 'Comida e Bebida'], ['Con', 'Construção Civil'], ['Edu', 'Educação'], ['Far', 'Farmacêutico'], ['Ges', 'Gestão de Resíduos'], ['Mat', 'Materias primas e químicos'], ['Mod', 'Moda e Têxtil'], ['Míd', 'Mídia'], ['Saú', 'Saúde'], ['Ser', 'Serviço'], ['Tec', 'Tech: TI e Software'], ['Tec', 'Tech: Hardware e Equipamentos'], ['Tec', 'Tech: Mobile'], ['Tur', 'Turismo'], ['Tel', 'Telecomunicações'], ['Var', 'Varejo'], ['Naú', 'Naútico'], ['Nav', 'Naval'], ['Emp', 'Empresas/Negócios (Business to Business)'], ['Con', 'Consumidores (Business to Consumer)'], ['Gov', 'Governo']], max_length=6),
        ),
    ]