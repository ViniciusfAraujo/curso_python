# idade_0 = 22
# idade_1 = 18

# if idade_0 >= 21 and idade_1 >= 21:
#     print(bool)

idade = 17
if idade >= 18:
    print('Você tem idade suficiente para votar')
else:
    print('Voce não pode votar')

print('-----------------------')

idade_0 = 2
if idade_0 < 4:
    price = 0
elif idade_0 < 18:
    price = 5
else:
    price = 10

print("Seu custo de admissão é $" + str(price) + '.')