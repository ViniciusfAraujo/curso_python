# Manipulando chaves e valores em dicionários
pessoa = {}


chave = 'nome'
pessoa[chave] = 'vinicius araujo'
pessoa['sobrenome'] = 'Araujo'

print(pessoa[chave])

pessoa[chave] = 'milena'
# del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

# print(pessoa.get('sobrenome', 'não existe'))

if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])

