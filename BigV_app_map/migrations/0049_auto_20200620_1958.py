# Generated by Django 3.0.7 on 2020-06-20 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BigV_app_map', '0048_auto_20200620_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dados_mapeamento',
            name='caso_outra',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
