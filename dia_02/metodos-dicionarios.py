# items() retorna todos os pares chave/conteúdo do dicionário.
# keys() retorna todas as chaves do dicionário.
# values() retorna todos os valores do dicionário.

cadastro = {'Jasmin': 1578956, 'Luan': 9864770, 'Liv': 8562225, 'Guilherme': 1203546}
print(cadastro.items())
# dict_items([('Jasmin', 1578956), ('Luan', 9864770), ('Liv', 8562225), ('Guilherme', 1203546)])

print(cadastro.keys())
# dict_keys(['Jasmin', 'Luan', 'Liv', 'Guilherme'])

print(cadastro.values())
# dict_values([1578956, 9864770, 8562225, 1203546])

# se um inteiro começar com zero, é preciso torná-lo um número suportado add 'o' após
cadastro['Théo'] = 0o214523
print(cadastro)

# laço percorrendo o dicionário
for x in cadastro:
    print(x)

# checando se determinado elemento pertence ao dicionário
print("Luan" in cadastro)
print("Théo" in cadastro)
print("Pietra" in cadastro)

# acessando chave
print(cadastro['Liv'])
