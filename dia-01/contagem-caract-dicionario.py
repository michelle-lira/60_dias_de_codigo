def contar_caracteres(s):
    """
    Função que conta os caracteres de uma string
    Ex:
    >>> contar_caracteres('uva')
    {'a': 1, 'u': 1, 'v': 1}
    >>> contar_caracteres('banana')
    {'a': 3, 'b': 1, 'n': 2}

    :param s: string a ser contada
    """
    resultado = {}

    for caracter in s:
        contagem = resultado.get(caracter, 0)
        contagem += 1
        resultado[caracter] = contagem

    return resultado


if __name__ == '__main__':
    print(contar_caracteres('tente um assobio'))
    print()
    print(contar_caracteres('grilo falante em pinoquio'))
