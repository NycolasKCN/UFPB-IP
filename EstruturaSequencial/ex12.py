"""Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule
seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58"""

def pesoIdeal(altura):
    return (72.7 * altura) - 58


altura = float(input("Digite o a sua altura em M (metros): "))

print(pesoIdeal(altura=altura))
