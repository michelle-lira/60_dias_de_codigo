# 10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit
celsius = float(input("Informe a temperatura em Celsius: "))
fahrenheit = ((celsius / 5.0) * 9.0) + 32.0

print(f"\nA temperatura em Farenheit é {fahrenheit:.1f} °F")

