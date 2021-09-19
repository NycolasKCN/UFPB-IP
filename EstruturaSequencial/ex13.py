"""Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu 
peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7"""

def pesoIdeal(sexo, altura):
    if sexo == "M":
        return (62.1 * altura) - 44.7

    elif sexo == "H":
        return (72.7 * altura) - 58

    else:
        print("Sexo invalido, tente novamente!")


sexo = input("Qual seu sexo: (para homem digite H e para mulher M) ").upper()[0]
altura = float(input("Digite a sua altura em M (metros): "))
peso_ideal = pesoIdeal(sexo, altura)

print(f"Seu peso ideal é de {peso_ideal:.1f}")
