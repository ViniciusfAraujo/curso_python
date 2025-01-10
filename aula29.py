"""
Dicionários em Python (tipo dict)
Dicionários são estruturas de dados do tipo
par de "chave" : "valor".
Chaves podem ser consideradas como "índice"
que vimos na lista e podem ser tipos imutáveis
como: str, int, float, bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro
dicionario.
Usamos as chaves - {} - ou a classe dict para criar
dicionários.
Imutáveis: str, int, float, bool, tuple
Mutável: dict, list
"""

pessoa = {
    'nome': 'Vinicius',
    'sobrenome': 'Araujo',
    'idade': 25,
    'altura': 1.9,
    'endereço': [
        {'rua': 'Av.Paramaribo', 'numero': 15}
    ]
}
# print(pessoa, type(pessoa))
print(pessoa['idade'])
print(pessoa['sobrenome'])
print()
for chave in pessoa:
    print(chave, pessoa[chave])