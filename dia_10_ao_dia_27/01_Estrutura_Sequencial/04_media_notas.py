# 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média. 
nota1 = float(input("Informe a primeira nota: [ex: 8.5] "))
nota2 = float(input("Informe a segunda nota: [ex: 8.5] "))
nota3 = float(input("Informe a terceira nota: [ex: 8.5] "))
nota4 = float(input("Informe a quarta nota: [ex: 8.5] "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"\nA media das notas bimestrais é: {media:.1f}")

