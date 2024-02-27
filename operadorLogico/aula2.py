# Operador Lógico "OR"
# Operadores lógico
# AND(e) OR(ou) NOT(não)
# OR - Qualquer condição verdadeira avalia toda expressao como verdadeira

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = 'vini1520'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')