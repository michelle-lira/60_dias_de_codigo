# 9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# Ex: C = 5 * ((F-32) / 9)
fahrenheit = float(input("Informe a temperatura em Farenheit: "))
celsius = 5 * ((fahrenheit - 32) / 9.0)

print(f"\nA temperatura em Celsius é {celsius:.1f} °C")

