#Interpolação de string com % em Python
# Interpolação básica de strings
# s - string
# d e i - int
# f - float
# x e X - hexadecimal (ABCDEF0123456789)
nome = 'vinicius'
preco = 100.51651211
variavel = '%s, o preço é R$%F' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))