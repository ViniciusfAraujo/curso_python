# crie funções que duplique, triplicam, quadruplicam o numero recebido como parametro.

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
tripicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(tripicar(2))
print(quadruplicar(2))