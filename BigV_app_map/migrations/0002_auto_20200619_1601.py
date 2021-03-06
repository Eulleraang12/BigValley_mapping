# Generated by Django 3.0.7 on 2020-06-19 19:01

from django.db import migrations, models
import localflavor.br.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('BigV_app_map', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dados_mapeamento',
            options={'verbose_name_plural': 'Dados_Mapeamento'},
        ),
        migrations.AddField(
            model_name='dados_mapeamento',
            name='bairro',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dados_mapeamento',
            name='cargo',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dados_mapeamento',
            name='cep',
            field=localflavor.br.models.BRPostalCodeField(default='', max_length=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dados_mapeamento',
            name='cidade',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dados_mapeamento',
            name='cnpj',
            field=localflavor.br.models.BRCNPJField(blank=True, max_length=18, null=True),
        ),
        migrations.AddField(
            model_name='dados_mapeamento',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dados_mapeamento',
            name='email_representante',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dados_mapeamento',
            name='estado',
            field=localflavor.br.models.BRStateField(default='', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dados_mapeamento',
            name='industria',
            field=models.BooleanField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dados_mapeamento',
            name='nome_representante',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dados_mapeamento',
            name='rua',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dados_mapeamento',
            name='site',
            field=models.URLField(blank=True, max_length=400),
        ),
        migrations.AddField(
            model_name='dados_mapeamento',
            name='telefone',
            field=phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128, region=None),
            preserve_default=False,
        ),
    ]
