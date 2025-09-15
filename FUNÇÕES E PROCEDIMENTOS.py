# Função e Procedimento

# FUNÇÕES -> subprograma que retorna algo

def nome_da_funcao(parametros):
     #código
     return # Usar o return em Python é uma forma de fazer uma função devolver um resultado para quem a chamou. Ele encerra a execução da função e envia o valor de volta.

#Ex.:

def somar_função(a, b):
    valor = a + b
    return f"total = {valor}" # Neste caso a função retorna o valor da soma, que é usado fora da função.

somar_função(2, 2)

# PROCEDIMENTO -> subprograma que não retorna nada, ou seja, não usa return

# Ex.:
def sem_return(a, b):
    print(a + b)

resultado = sem_return(2, 3) # A função é chamada com os argumentos 2 e 3. O print(a + b) dentro da função executa e exibe 5 no console.
# Porém, como a função não retorna nada, o valor armazenado à variável resultado é None (que é o valor padrão de retorno em Python quando não se usa return).

print(resultado)  # Saída: 5 (da função) e depois None (resultado)

# Se fosse sem a variável resultado:

sem_return(2, 3) # A função é chamada com os argumentos 2 e 3. O print(a + b) dentro da função executa e exibe 5 no console. O None que aparecia anteriormente (quando havia a variável resultado) só não aparece pois ele não tem onde ser armazenado, já antes ele aparecia pois era armazenado na variável resultado depois impresso

# Esse código, em Python, tecnicamente tudo é uma "função" (porque usamos def), mas o comportamento dele é de procedimento. Pois ele apenas executa uma ação (imprime algo), mas não "retorna" resultado algum para quem o chamou, já que não tem return

#Assim, a diferença entre usar essas formas de chamada, é que se você quiser armazenar o valor do return você vai usar de uma variável, se não você pode apenas chamar a função
#Ex.:
def abc():
    valor = 1+1
    print(valor)
    return valor
abc() #Retorna 2
a = abc()
print(a) #Retorna 2\n2

# return -> vai devolver algo como resposta
# print -> é uma função que só faz parte do código, assim tendo que ser executada, ela irá apenas imprimir na tela um parâmetro, mas não irá responder algo

# Desempacotando Valores

def operacoes(a, b):
    soma = a + b
    subtracao = a - b

    return soma, subtracao # Em Python, isso retorna uma tupla com dois elementos.

x, y = operacoes(10, 3) # Chama a função operacoes com a = 10 e b = 3.
# A função retorna (13, 7), ou seja, x = 13 e y = 7. Pois a tupla criada pelo return vai ser descompactada entre a variável x e y.
# Obs.: Se ouver mais valores na tupla que variáveis para desempacotar o código irá gerar um erro.

print("Soma:", x)         # Saída: 13
print("Subtração:", y)    # Saída: 7
