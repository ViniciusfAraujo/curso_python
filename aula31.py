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

pessoa = {
    'nome': 'Vinicius',
    'sobrenome': 'Araujo',
}

pessoa.setdefault('idade', 25)
print(pessoa['idade'])
# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))

# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)
