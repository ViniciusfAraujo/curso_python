def buscarMenor(array):
    menor = array[0]
    menor_indice = 0
  
    for i in range(1, len(array)):
        if array[i] < menor:
            menor = array[i]
            menor_indice = i
  
    return menor_indice
  
def ordenacaoSelecao(array):
    novo_array = []
  
    for i in range(len(array)):
        menor = buscarMenor(array)
        novo_array.append(array.pop(menor))
  
    return novo_array
  
print(ordenacaoSelecao([5, 3, 6, 2, 10]))
