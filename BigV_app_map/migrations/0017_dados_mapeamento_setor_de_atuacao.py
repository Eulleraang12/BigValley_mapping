# Generated by Django 3.0.7 on 2020-06-20 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BigV_app_map', '0016_auto_20200620_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='dados_mapeamento',
            name='setor_de_atuacao',
            field=models.CharField(blank=True, choices=[('industria', 'Indústria'), ('comercio', 'Comercio'), ('servico', 'Serviços')], max_length=20),
        ),
    ]