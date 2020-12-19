# Generated by Django 3.1.4 on 2020-12-15 18:57

from django.db import migrations, models
import localflavor.br.models
import multiselectfield.db.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('BigV_app_map', '0053_auto_20200620_2041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dados_Mapeamento_empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=10)),
                ('pessoa', models.CharField(choices=[('PF', 'Pessoa Física'), ('PJ', 'Pessoa Jurídica')], default='', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Dados_Mapeamento_Empresa',
            },
        ),
        migrations.CreateModel(
            name='Dados_Mapeamento_startup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('site', models.URLField(blank=True, max_length=400)),
                ('email', models.EmailField(max_length=254)),
                ('cnpj', localflavor.br.models.BRCNPJField(blank=True, max_length=18, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='BigV_app_map/static/media_root')),
                ('cep', localflavor.br.models.BRPostalCodeField(default='', max_length=9)),
                ('rua', models.CharField(default='', max_length=100)),
                ('bairro', models.CharField(default='', max_length=100)),
                ('cidade', models.CharField(default='', max_length=100)),
                ('estado', localflavor.br.models.BRStateField(max_length=2)),
                ('nome_representante', models.CharField(default='', max_length=100)),
                ('cargo', models.CharField(default='', max_length=20)),
                ('telefone', phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128, region=None)),
                ('email_representante', models.EmailField(default='', max_length=254)),
                ('setor_de_atuacao', multiselectfield.db.fields.MultiSelectField(choices=[('ind', 'Indústria'), ('com', 'Comércio'), ('ser', 'Serviços')], max_length=11)),
                ('area_de_atuacao_da_startup', models.CharField(default='', max_length=1000)),
                ('segmento_area', models.CharField(choices=[['Aer', 'Aeronáutico/Aeroespacial'], ['Agr', 'Agronégocio'], ['Arq', 'Arquitetura e Designer'], [' Ar', ' Arte e Cultura'], ['Aut', 'Automotivo'], ['Bel', 'Beleza'], ['Bio', 'Biotecnologia'], ['Com', 'Comida e Bebida'], ['Con', 'Construção Civil'], ['Edu', 'Educação'], ['Far', 'Farmacêutico'], ['Ges', 'Gestão de Resíduos'], ['Mat', 'Materias primas e químicos'], ['Mod', 'Moda e Têxtil'], ['Míd', 'Mídia'], ['Saú', 'Saúde'], ['Ser', 'Serviço'], ['Tec', 'Tech: TI e Software'], ['Tec', 'Tech: Hardware e Equipamentos'], ['Tec', 'Tech: Mobile'], ['Tur', 'Turismo'], ['Tel', 'Telecomunicações'], ['Var', 'Varejo'], ['Naú', 'Naútico'], ['Nav', 'Naval'], ['Emp', 'Empresas/Negócios (Business to Business)'], ['Con', 'Consumidores (Business to Consumer)'], ['Gov', 'Governo']], default='', max_length=100)),
                ('detalhes_de_area_de_atuacao', models.CharField(default='', max_length=1000)),
                ('segmento_de_atuacao', models.CharField(choices=[['Aer', 'Aeronáutico'], ['Agr', 'Agronégocio'], ['Arq', 'Arquitetura e Design'], ['Aut', 'Automotivo'], ['Bel', 'Beleza'], ['Bio', 'Biotecnologia'], ['Com', 'Comida e Bebida'], ['Con', 'Construção Civil'], ['Edu', 'Educação'], ['Far', 'Farmacêutico'], ['Ges', 'Gestão de Resíduos'], ['Mat', 'Matérias Primas e Químicos'], ['Mod', 'Moda e Textil'], ['Mid', 'Midia'], ['Saú', 'Saúde e Bem-estar'], ['Ser', 'Serviço'], ['Tec', 'Tech: TI e Software'], ['Tec', 'Tech: Hardware e Equipamentos'], ['Tec', 'Tech: Mobile'], ['Tel', 'Telecomunicações'], ['Var', 'Varejo'], ['Naú', 'Naútico'], ['Nav', 'Naval'], ['Art', 'Arte e Cultura'], ['Tur', 'Turismo']], default='', max_length=100)),
                ('tipo_de_cliente', models.CharField(choices=[('B2B', 'Empresas e Negócios (B2B) '), ('B2C', 'Consumidores (B2C) '), ('GOV', 'Governo')], default='', max_length=100)),
                ('possui_mercado_global', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=True)),
                ('possui_Influencia_ou_interesse_militar', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=True)),
                ('qual_estrategia_de_saida_ou_idealizada_para_o_negocio', multiselectfield.db.fields.MultiSelectField(choices=[('cre', 'Crescimento Lucrativo para o Mercado Global '), ('aqu', 'Aquisição por uma Grande Empresa'), ('fus', 'Fusão com outra empresa'), ('ofe', 'Oferta Pública Inicial de Ações')], default=0, max_length=15)),
                ('sua_startup_possui_conhecimento_ou_e_treinada_nas_metodologias_descritas_abaixo', multiselectfield.db.fields.MultiSelectField(choices=[('lsu', 'Lean Start up '), ('mod', 'Modelo de Negócios'), ('des', 'Designer Thinking'), ('out', 'Outras ?')], default=0, max_length=15)),
                ('caso_outra', models.CharField(blank=True, max_length=100, null=True)),
                ('startup_foi_fundada_dentro_dos_5_anos_de_graduacao_dos_fundadores', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=True)),
                ('numero_de_socios', models.CharField(default='', max_length=255)),
                ('ano_de_fundacao', models.CharField(default='', max_length=4)),
                ('ja_foi_investida', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=True)),
                ('quantas_rodadas', models.CharField(default='', max_length=255)),
                ('montante_investido', models.CharField(default='', max_length=255)),
                ('quais_os_modelos_de_receitas_se_enquadra_no_perfil_da_empresa_startup', models.CharField(choices=[['Ven', 'Venda Unitária (Produto)'], ['Ven', 'Venda Direta'], ['Ven', 'Venda Indireta (agentes ou representantes)'], ['Fre', 'Freemium'], ['Sof', 'Software as a service (SaaS)'], ['Rec', 'Receita com anúncios'], ['Lic', 'Licença por usuário'], ['Lic', 'Licença por produto'], ['Suc', 'Sucessfee'], ['Hom', 'Homem hora'], ['Com', 'Comissão'], ['Mar', 'Markup'], ['Oth', 'Other']], default='', max_length=100000)),
                ('quais_programas_iniciativas_movimentos_de_empreendedorismo_e_inovacao_que_participa', models.TextField(default='', max_length=100000)),
                ('com_quais_entidades_do_ecossistema_tem_conexao_interacao_frequente_projetos_em_parceria_colaboracao_que_contribuiram_e_contribuem_para_as_inovacoes_e_aperfeicoamento_da_empresa', models.TextField(default='', max_length=100000)),
                ('estes_parceiros_listados_acima_possuem_que_esfera', multiselectfield.db.fields.MultiSelectField(choices=[('reg', 'Regional'), ('est', 'Estadual'), ('nac', 'Nacional'), ('int', 'Internacional')], default=0, max_length=15)),
            ],
            options={
                'verbose_name_plural': 'Dados_Mapeamento_Startup',
            },
        ),
        migrations.DeleteModel(
            name='Dados_Mapeamento',
        ),
    ]
