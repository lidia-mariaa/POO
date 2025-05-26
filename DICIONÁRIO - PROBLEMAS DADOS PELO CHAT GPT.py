# Receba um texto. Crie um dicionário onde a chave é cada palavra única, e o valor é outro dicionário com:

# Número de ocorrências

# Primeira posição no texto (índice da palavra)

# Última posição no texto

# Entrada:
# "olá mundo olá mundo teste"

# Saída:
# {
#   "olá": {"ocorrencias": 2, "primeira": 0, "ultima": 2},
#   "mundo": {"ocorrencias": 2, "primeira": 1, "ultima": 3},
#   "teste": {"ocorrencias": 1, "primeira": 4, "ultima": 4}
# }

texto = "Estudando para a prova"

palavras = texto.split()
dicionário = {}
for i in range(len(palavras)):
    if palavras[i] in dicionário:
        dicionário[palavras[i]["ocorrencia"]] += 1
        dicionário[palavras[i]["ocorrencia"]] = i
    else:
        dicionário[palavras[i]] = {
            "ocorrencia" : 1,
            "primeira" : i,
            "ultima" : i
            }
print(dicionário)

# Dado um dicionário com alunos e suas médias:

# python
# Copiar
# Editar
# alunos = {
#   'Ana': 8.9,
#   'Bruno': 6.5,
#   'Clara': 4.2,
#   'Daniel': 9.7,
#   'Elisa': 7.0,
#   'Fernando': 3.9
# }
# Agrupe os nomes dos alunos por faixa de nota:

# 0–4.9 → "Insuficiente"

# 5–6.9 → "Regular"

# 7–8.9 → "Bom"

# 9–10 → "Excelente"

# Saída esperada:

# {
#   "Insuficiente": ['Clara', 'Fernando'],
#   "Regular": ['Bruno'],
#   "Bom": ['Ana', 'Elisa'],
#   "Excelente": ['Daniel']
# }

alunos = {
  'Ana': 8.9,
  'Bruno': 6.5,
  'Clara': 4.2,
  'Daniel': 9.7,
  'Elisa': 7.0,
  'Fernando': 3.9
}
diário = {}
insuficientes = []
regular = []
bom = []
exelente = []
for alunos_chave in alunos:
    if 0 <= alunos[alunos_chave] <= 4.9:
        insuficientes.append(alunos_chave)
    elif 5 <= alunos[alunos_chave] <= 6.9:
        regular.append(alunos_chave)
    elif 7 <= alunos[alunos_chave] <= 8.9:
        bom.append(alunos_chave)
    else:
        exelente.append(alunos_chave)
    diário["insuficientes"] = insuficientes
    diário["regular"] = regular
    diário["bom"] = bom
    diário["exelente"] = exelente
print(diário)
