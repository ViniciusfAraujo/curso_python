"""
Listas em Python
Tipo list - Mútavel
Suporta vários valores em qualquer tipo
Conhecimento reutilizaveis - indice e fatiamento
Método úteis: append, insert, pop, del, clear, extend, + 
"""

#--------+01234
#---------54321
string = "ABCDE" # 5 caracteres (len)
# print(bool([])) falsy
# print(lista, type(lista))

lista = [123, True, "Vinicius", 1.2, []]
lista[2] = "joao" 
print(lista[2], type(lista[2]))
print(lista)