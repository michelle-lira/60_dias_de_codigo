"""
11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

    a. o produto do dobro do primeiro com metade do segundo.
    b. a soma do triplo do primeiro com o terceiro.
    c. o terceiro elevado ao cubo. 
"""
import math

num_int_1 = int(input("Informe um numero inteiro: "))
num_int_2 = int(input("Informe outro numero inteiro: "))
num_real = float(input("Informe um numero real: [ex: 99.5] "))

a = (2 * num_int_1) * (num_int_2 / 2)
b = (3 * num_int_1) + num_real
c = math.pow(num_real, 3)

print(f"\nO dobro do primeiro vezes a metade do segundo é: {a}")
print(f"A soma do triplo do primeiro com o terceiro é: {b}") 
print(f"O terceiro elevado ao cubo é: {c:.1f}")

