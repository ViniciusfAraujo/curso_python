def binary_search(arr, elemento):
    esquerda, direita = 0, len(arr) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if arr[meio] == elemento:
            return meio
        elif arr[meio] < elemento:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1

# Exemplo de uso:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elemento = 10
indice = binary_search(arr, elemento)

if indice != -1:
    print(f"O elemento {elemento} está na posição {indice}.")
else:
    print("O elemento não está na lista.")