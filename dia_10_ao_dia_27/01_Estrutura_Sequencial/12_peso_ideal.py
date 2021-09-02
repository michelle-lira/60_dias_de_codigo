# 12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
# usando a seguinte fórmula: (72.7*altura) - 58
altura = float(input("Informe a sua altura: [ex: 1.70] "))

peso_ideal = (72.7 * altura) - 58

print(f"\nO seu peso ideal é: {peso_ideal:.1f}")

