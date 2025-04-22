#Recuperação de POO
#Questão 1
while True:
    #nota = int(input("Informe uma nota entre 0 e 10"))
    nota_str = input("Informe uma nota entre 0 e 10")
    if nota_str.isdigit():
        nota = int(nota_str)
        if 0 <= nota <= 10:
            print(f"A nota {nota} válida")
        else:
            print(f"A nota {nota} é inválida")
    else:
        print("Valor inserido inválido")
