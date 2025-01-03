def multiplicar(*args):
    total = 1
    for numeros in args:
        total *= numeros
    return total

# mult_1_2_3 = multiplicar(1,2,3)
# print(mult_1_2_3)
# print(1*2*3)

mult_4_5_6_7_8 = multiplicar(4,5,6,7,8)
print(mult_4_5_6_7_8)
print(4*5*6*7*8)

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'

print(par_impar(2))
print(par_impar(3))
print(par_impar(6))
print(par_impar(16))
print(par_impar(15))
