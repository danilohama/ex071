""" Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte qual será o valor a ser saca
do (Numero inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20 R$10 e R$1 """
print('==' * 30)
print('{:^30}'.format('Banco Danilo SA'))
print('==' * 30)
valor = int(input('Qual valor quer sacar? R$'))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print('Total de {} cédulas de R${}'.format(totalced, ced))
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('==' * 30)
print('TRANSAÇÃO FINALIZADA COM SUCESSO! VOLTE SEMPRE')
