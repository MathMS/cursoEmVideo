"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão."""

t = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão da PA: "))
soma = r + t
print('{} + {} = {}'.format(t, r, soma))
for c in range(1,10):
    print('{} + {} = {}'.format(soma, r, soma+r))
    soma = r + soma