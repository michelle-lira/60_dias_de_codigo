# 6. Faça um programa que peça o raio de um círculo, calcule e mostre sua área.
import math

raio = int(input("Digite o valor da medida do raio de um círculo: "))
area = (2 * math.pi * raio)

print(f"\nUm círculo com raio {raio} possui área igual a {area:.2f}.")

