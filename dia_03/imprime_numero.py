# Faça um Programa que peça um número e então mostre a mensagem:
# O número informado foi [número].
# Obs: O programa precisa funcionar tanto na versão 2 do python, quanto na versão 3.

import sys

if sys.version_info.major == 2:
    num = raw_input('Digite um número: ')
elif sys.version_info.major == 3:
    num = input('Digite um número: ')

print(f'O número digitado foi: {num}')
