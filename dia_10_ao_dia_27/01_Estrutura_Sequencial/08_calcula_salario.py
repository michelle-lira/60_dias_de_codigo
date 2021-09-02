# 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês:
valor_por_hora = float(input("Qual o valor da sua hora trabalhada: "))
horas_trabalhadas = float(input("Informe a quantidade de horas trabalhadas: "))

salario = (valor_por_hora * horas_trabalhadas)

print(f"\nSeu salario neste mês será de R$ {salario:.2f}")

