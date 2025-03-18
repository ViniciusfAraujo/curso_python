"""
Métodos úteis dos dicionarios em python
len - quantas chaves
keys - iterável com as chaves
values - iterável com valores 
items - iterável com chaves e valores
setdefault - adicionar valor se a chave não existe
copy - retorna uma cópia rasa
get - obtém uma chave
pop - apaga um item com a chave especifica (del)
popitem - apaga o ultimo item adicionado 
update - atualiza um dicionario com outro
"""
import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2]
}

d2 = copy.deepcopy(d1)

d2['c1'] = 1000
d2['l1'][1] = 99999
print(d1)
print(d2)