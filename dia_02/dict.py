string = input("Digite uma string: ")
conta = {}  # dicionário vazio
for letra in string:
    if letra in conta:
        conta[letra] += 1
    else:
        conta[letra] = 1  # adiciona letra no dicionário
letramais = ''
for key in conta:
    if not letramais:  # nenhuma mais comum ainda
        letramais = key
    elif conta[key] > conta[letramais]:
        letramais = key
print(letramais)
