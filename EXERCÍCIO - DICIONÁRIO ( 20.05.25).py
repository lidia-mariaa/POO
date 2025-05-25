# Questão 1: Dada uma string, crie um dicionário que conte a frequência de cada palavra na string. Ignore diferenças entre maiúsculas e minúsculas.
# Exemplo:
# texto = "O rato roeu a roupa do rei de Roma. O rato é esperto."
# Saída esperada (aproximada): {'o': 2, 'rato': 2, 'roeu': 1, ...}

texto = "O rato roeu a roupa do rei de Roma. O rato é esperto."
palavras = texto.split()
contagem = {}
for i in palavras: #Quando não usamos o range + o len(), a variável i será, inicialmente, o primeiro valor presente na lista, depois o segundo, e assim em diante
    if i in contagem:
        contagem[i] += 1
    else:
        contagem[i] = 1
print(contagem)

#forma de fazer usando o range + o len():

# for i in range(len(palavras)):
#     if palavras[i] in contagem:
#         contagem[palavras[i]] += 1
#     else:
#         contagem[palavras[i]] = 1
# print(contagem)

# Agrupamento por Categoria:
# Questão 2: Você tem uma lista de itens, onde cada item é um dicionário com um campo "categoria". Crie um dicionário onde as chaves são as categorias e os valores são listas de itens pertencentes a cada categoria.
# Exemplo:

# Saída esperada: {
  #   'Fruta': [{'nome': 'Maçã', 'categoria': 'Fruta'},
  #             {'nome': 'Banana', 'categoria': 'Fruta'}],
  # 'Vegetal': [{'nome': 'Cenoura', 'categoria': 'Vegetal'},
  #             {'nome': 'Alface', 'categoria': 'Vegetal'}]}

lista = [
    {"nome": "Maçã", "categoria": "Fruta"}, # Item 1, tipo DIC
    {"nome": "Banana", "categoria": "Fruta"}, # Item 2
    {"nome": "Cenoura", "categoria": "Vegetal"}, # Item 3
    {"nome": "Alface", "categoria": "Vegetal"}, # Item 4
]

dicionário = {} #onde vai ficar armazenado tudo

for item in lista: #a variável item vai armazenar os dicionários
    if item['categoria'] in dicionário:
        dicionário[item["categoria"]].append(item['nome']) #podemos usar append pois dicionário[item["categoria"]] é uma lista, como afirma a linha 49
    else:
        lista_2 = [item['nome']]
        dicionário[item["categoria"]] = lista_2
print(dicionário)

# Dicionário de Dicionários (Aninhamento):
# Questão 3: Você tem dados sobre estudantes, onde cada estudante tem um nome e uma lista de notas em diferentes disciplinas. Organize esses dados em um dicionário onde a chave é o nome do estudante e o valor é outro dicionário contendo as notas por disciplina. Calcule a média de cada aluno.
# Exemplo:
# dado_estudantes = [
#     {"nome": "Alice", "notas": {"Matemática": 8.5, "Português": 9.0}},
#     {"nome": "Davi", "notas": {"Matemática": 7.0, "História": 8.0, "Geografia": 6.5}},
# ]
# Saída esperada (aproximada):
# {
#     'Alice': {'Matemática': 8.5, 'Português': 9.0, 'media': 8.75},
#     'Davi': {'Matemática': 7.0, 'História': 8.0, 'Geografia': 6.5, 'media': 7.17}
# }

dado_estudantes = [
    {"nome": "Alice", "notas": {"Matemática": 8.5, "Português": 9.0}},
    {"nome": "Davi", "notas": {"Matemática": 7.0, "História": 8.0, "Geografia": 6.5}},
]
dicionário_estudantes = {}
for alunos in dado_estudantes: #alunos estará armazenando o dicionário de cada aluno
    notas = alunos['notas'] #essa variável irá armazenar o dicionário de notas
    media = (sum(notas.values()))/len(notas) #vai calcular a media
    dicionário_estudantes[alunos['nome']] = [notas, media] #vai criar uma chave com o nome de cada aluno e armazenar nela seu dicionário de notas e sua média
print(dicionário_estudantes)
