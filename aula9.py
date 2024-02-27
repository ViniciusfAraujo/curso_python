#Uma introdução às f-strings (formatação de strings)
nome = 'Vinicius'
altura = 1.90
peso = 91
imc = peso/altura ** 2

# f-string
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc e {imc:.2f}'

print(linha_1)
print(linha_2)
# print('pesa', peso, 'quilos e seu imc e', imc)

