"""
13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7 
"""
sexo = input("Informe seu sexo [M/F]: ").capitalize()
altura = float(input("Informe sua altura em metros [ex: 1.70]: "))
peso = float(input("Informe o seu peso em kg [ex: 80.5]: "))

if (sexo == "M"):
    peso_ideal = (72.7 * altura) - 58
    print(f"\nO seu peso ideal é: {peso_ideal:.1f}.")
else:
    peso_ideal = (62.1 * altura) - 44.7
    print(f"\nO seu peso ideal é: {peso_ideal:.1f}.")
    
if peso > peso_ideal:
    compara_peso = peso - peso_ideal
    print(f"\nVocê precisa perder {compara_peso:.1f} kg para ficar com o peso ideal para a sua altura.")
elif peso == peso_ideal:
    print("Você está com o peso ideal para a sua altura.")
elif peso < peso_ideal:
    compara_peso_2 = peso_ideal - peso
    print(f"\nVocê está com {compara_peso_2:.1f} kg a menos do que o peso ideal para a sua altura.")

