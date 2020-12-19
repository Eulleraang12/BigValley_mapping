def seg_area_lazy():
    setores = ['Aeronáutico/Aeroespacial',
            "Agronégocio","Arquitetura e Designer",
        " Arte e Cultura","Automotivo","Beleza",
        'Biotecnologia',"Comida e Bebida",'Construção Civil',
        "Educação","Farmacêutico","Gestão de Resíduos",
        "Materias primas e químicos",
        "Moda e Têxtil",'Mídia','Saúde',"Serviço",
        'Tech: TI e Software',"Tech: Hardware e Equipamentos",
        'Tech: Mobile','Turismo','Telecomunicações',
        'Varejo','Naútico','Naval','Empresas/Negócios (Business to Business)',
        'Consumidores (Business to Consumer)','Governo',
            ]
    y = []
    for setor in setores:
        x = ['{}'.format(setor[0:3]), '{}'.format(setor)]
        y.append(x)
    return y

def seg_atu_lazy():
    setores = ['Aeronáutico', "Agronégocio", 'Arquitetura e Design', 'Automotivo',
                'Beleza','Biotecnologia','Comida e Bebida','Construção Civil','Educação',
                'Farmacêutico','Gestão de Resíduos','Matérias Primas e Químicos','Moda e Textil',
                'Midia','Saúde e Bem-estar','Serviço','Tech: TI e Software',"Tech: Hardware e Equipamentos",
                'Tech: Mobile','Telecomunicações','Varejo','Naútico','Naval','Arte e Cultura','Turismo',
            ]
    y = []
    for setor in setores:
        x = ['{}'.format(setor[0:3]), '{}'.format(setor)]
        y.append(x)
    return y

def receita_lazy():

    setores = [ 'Venda Unitária (Produto)','Venda Direta','Venda Indireta (agentes ou representantes)',
                'Freemium','Software as a service (SaaS)','Receita com anúncios','Licença por usuário',
                'Licença por produto','Sucessfee','Homem hora','Comissão','Markup','Other',
            ]
    y = []
    for setor in setores:
        x = ['{}'.format(setor[0:3]), '{}'.format(setor)]
        y.append(x)
    return y


def capital_humano_lazy():

    setores = [ 'Empreendedores','Especialistas - Talentos Técnicos e Criativos','Professores / Pesquisadores',
               'Inventores', 'Academia / Curso Técnico e Graduação'
            ]
    y = []
    for setor in setores:
        x = ['{}'.format(setor[0:3]), '{}'.format(setor)]
        y.append(x)
    return y

def suporte_lazy():

    setores = [ "Organizações Integrativas","Serviços de Suporte a Negócios e ao Ecossistema","Coaches",'Consultores',
               'Acessores','Mentores',
            ]
    y = []
    for setor in setores:
        x = ['{}'.format(setor[0:3]), '{}'.format(setor)]
        y.append(x)
    return y

