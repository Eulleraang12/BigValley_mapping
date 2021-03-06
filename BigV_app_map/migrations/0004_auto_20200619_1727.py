# Generated by Django 3.0.7 on 2020-06-19 20:27

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('BigV_app_map', '0003_auto_20200619_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='dados_mapeamento',
            name='area_atu',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dados_mapeamento',
            name='telefone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='BR'),
        ),
    ]
