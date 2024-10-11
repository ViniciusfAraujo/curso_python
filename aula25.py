"""
    apeend - Adiciona um item ao final
    insert - Adiciona um item no indice escolhido
    pop - Remove do final ou do indice escolhido
    del - apaga um indice
    clear - limpa a lista 
    extend - extende a lista 
    + - concatena listas

Create Read Update Delete
Criar, Ler, Alterar, Apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]
lista.append('Vinicus')
nome = lista.pop()
lista.append(1233)
del lista[-1]
lista.insert(0, 5)
print(lista[2])


lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)