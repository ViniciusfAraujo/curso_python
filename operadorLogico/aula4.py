# Operadores IN e NOT IN
# Strings são iteravéis
#  0 1 2 3 4 5 6 7 
#  v i n i c i u s
# -8-7-6-5-4-3-2-1

# nome ='Vinicius'
# print(nome[7])
# print('ius' in nome)
# print('f' in nome)
# print(10 * '-')
# print('ius' not in nome)
# print('f' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite oque deseeja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else: 
    print(f'{encontrar} nãao esta em {nome}')