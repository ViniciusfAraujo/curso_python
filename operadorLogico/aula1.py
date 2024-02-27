# Operador Lógico "AND"
# Operadores lógico
# AND(e) OR(ou) NOT(não)
# AND - Todas as condiçoes precisam ser verdadeiras

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = 'vini1520'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

