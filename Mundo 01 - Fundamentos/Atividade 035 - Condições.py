'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas odem ou não formar um triângulo'''

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('\033[34mForma um triângulo!\033[m')
else:
    print('\033[33mNão forma um triângulo!\033[m')