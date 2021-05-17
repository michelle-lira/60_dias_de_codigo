"""
Contando Letras -> Dicionário
● Faça uma função que dada uma string, retorna a letra mais comum nessa string (em caso de empate
retorne qualquer uma das mais frequentes).
    ○ Ideia: usar um dicionário para contar cada letra.
    ○ A letra é a chave do dicionário, e o valor será quantas vezes a letra foi encontrada.
"""
frase = input('Digite uma frase: \n')
conta = {}

for letra in frase:
    if letra in conta:
        conta[letra] += 1
    else:
        conta[letra] = 1

letramais = ''
for key in conta:
    if not letramais:
        letramais = key
    elif conta[key] > conta[letramais]:
        letramais = key

print(letramais)
