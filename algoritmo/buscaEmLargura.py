from collections import deque

grafo = {
    'voce': ['alice', 'bobm',  'claire'],
    'bob': ['anjum', 'peggy'],
    'alice': ['peggy'],
    'claire': ['thom', 'jonny'],
    'anjum': [],
    'peggy': [],
    'thom': [],
    'jonny': []
}

def pessoa_eh_vendedor(nome):
    return nome[-1] == 'm'

def pesquisar(nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[nome]
    verificado = set()  

    while fila_de_pesquisa:
        pessoa_atual = fila_de_pesquisa.popleft()
        if pessoa_atual not in verificado:
            if pessoa_eh_vendedor(pessoa_atual):
                print(f'{pessoa_atual} é vendedor de manga')
                return True
            else:
                fila_de_pesquisa += grafo[pessoa_atual]
                verificado.add(pessoa_atual)

    print('Sem vendedor de manga')
    return False

pesquisar('voce')
