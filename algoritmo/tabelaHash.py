dicio = {'chave': 'valor'}
caderno = dict()
caderno["maca"] = 0.67
caderno["leite"] = 1.67
caderno["abacate"] = 2.47

print(caderno["maca"])
print(type(dicio))

votaram = {}
voted = {}

def verificar_eleitor(nome):
    if nome in votaram:
        print('Mandem embora!')
    else:
        if voted.get(nome) is None:
            voted[nome] = True
            print('Deixe votar!')
        else:
            print('Mandem embora!')

verificar_eleitor('tom')
verificar_eleitor('mike')
verificar_eleitor('mike')

