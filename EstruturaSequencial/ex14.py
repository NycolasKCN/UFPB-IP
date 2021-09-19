"""João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento 
diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo 
regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo 
excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) 
e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e 
na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as
mensagens adequadas."""

limitePeso = 50 # quilos é o limite de peso
multa = 4 # reais por quilo

pesoPeixe = float(input("Digite em quantos kilos você pescou hoje: (em kilos) "))
excessoPeso = pesoPeixe - limitePeso

if excessoPeso <= 0:
    print("Parabéns jõao você não tera que pagar nenhuma multa!!")
    print(f"Você pescou {pesoPeixe} Kg hoje!")

elif excessoPeso > 0:
    multa *= excessoPeso
    print("joão hoje pescou mais que o limite! :(")
    print(f"Você pescou além do limite {excessoPeso} e sua multa será de R${multa:.2f}")
    print(f"Você pescou ao total {pesoPeixe}Kg")