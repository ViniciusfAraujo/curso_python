"""
get - obtém uma chave
pop - apaga um item com a chave especifica (del)
popitem - apaga o ultimo item adicionado 
update - atualiza um dicionario com outro

"""



p1 ={
    'nome': 'Vinicius',
    'sobrenome':'Araujo'
}

# print(p1.get('nome'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)

# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

# p1.update({
#     'nome': 'novo valor',
#     'idade': 25 
# })

# print(p1)

# p1.update(nome="novo valor", idade=25)
tupla = ('nome', 'novo valor'), ('idade', 25)
lista = ['nome', 'novo valor'], ['idade', 25]
p1.update(lista)
print(p1)