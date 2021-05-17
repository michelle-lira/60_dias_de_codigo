print('-='*28)
print('=-=-=', 'SAIBA SE VOCÊ FOI APROVADO EM UMA DISCIPLINA', '=-=-=')
print('-='*28)
print()


def calcula_media_disciplina(nota1, nota2, nota3):
    """Função para calcular a média semestral do aluno em apenas 1 disciplina
    :param nota1: número
    :param nota2: número
    :param nota3: número
    """
    disciplina = input("Você deseja calcular a média de qual disciplina? ")
    media = float((nota1 + nota2 + nota3) / 3)
    print(f'\nA sua média em {disciplina} é: {media:.1f}.\n')


def informa_status_aluno(media):
    """Função para informar o status do aluno no semestre em 1 disciplina
    :param media: número
    """
    if media >= 7.0:
        print('-> Você está APROVADO por média.')
        if media > 9.0:
            print('*-'*3, 'Parabéns! Você alcançou nota máxima.', '-*'*3)
    elif media >= 4.0:
        print('-> Você deve fazer prova de RECUPERAÇÃO.')
    else:
        print('-> Você foi REPROVADO. Estude um pouco mais no próximo semestre.')


calcula_media_disciplina(10, 10, 10)
informa_status_aluno(10)
