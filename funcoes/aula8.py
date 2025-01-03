#  Closure e funções que retornam outras funções

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia' )
falar_boa_noite = criar_saudacao('Boa noite')

# print(falar_bom_dia('Milena'))
# print(falar_boa_noite('Vinicius'))

for nome in ['Isabel', 'Jose', 'Ana paula']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))