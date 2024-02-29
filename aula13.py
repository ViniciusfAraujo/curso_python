"""
Formatação básica de strings
s - string
d - int
f - float
.<Número de dígitos>f
x ou X - hexadecimal
(Caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
Sinal - + ou -
Ex.: >-100,.f
Conversion flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel:.^11}')
print(f'{1000.054651121286121:.2f}')