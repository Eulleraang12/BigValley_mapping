# Generated by Django 3.1.4 on 2020-12-19 03:48

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('BigV_app_map', '0066_auto_20201219_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dados_mapeamento_startup',
            name='telefone',
            field=phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128, region=None),
        ),
    ]