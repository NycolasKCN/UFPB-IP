"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o 
Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.

calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

from os import system

valor_da_hora = float(input("Digite quanto você ganha por hora: R$"))
horas_trabalhadas = int(input("Digite quantas horas você trabalhou no mês: "))

salario_bruto = horas_trabalhadas * valor_da_hora

imposto_de_renda = salario_bruto * (11/100)
inss = salario_bruto * (8/100)
sindicato = salario_bruto * (5/100)

salario_liquido = salario_bruto - (imposto_de_renda + inss + sindicato)

system("cls")

print("+ {:<15} : R$ {:>10.2f}".format("Salário Bruto", salario_bruto))
print("- {:<15} : R$ {:>10.2f}".format("IR (11%)", imposto_de_renda))
print("- {:<15} : R$ {:>10.2f}".format("INSS (8%)", inss))
print("- {:<15} : R$ {:>10.2f}".format("Sindicato (5%)", sindicato))
print("= {:<15} : R$ {:>10.2f}".format("Salário Liquido", salario_liquido))
