"""Cláudia tem uma loja de conveniência e precisa de um programa para gerenciar o cálculo e a liberação de troco no estabelecimento. 
Ela deseja informar o valor que o cliente pagou e o valor do produto comprado, e espera que o programa informe quanto será o troco, 
e como ele deverá ser entregue: quantas cédulas de R$ 5, quantas cédulas de R$ 2 e quantas moedas de R$ 1. Ajude Lidiane escrevendo 
esse programa em Python. (Obs: considere que o cliente sempre terá dinheiro suficiente para pagar o produto, que as entradas são inteiras, 
e que não há outras cédulas e moedas possíveis para troco. Dica: pense em divisão)"""

valorPago = int(input("Digite o valor que o cliente pagou: R$"))
valorProduto = int(input("Digite o valor do produto: R$"))

troco = valorPago - valorProduto

print(f"Troco total: R${troco:.2f}")

notasDe5 = troco // 5
notasDe2 = (troco - (notasDe5 * 5)) // 2
moedasDe1 = (troco - ((notasDe5 * 5) + (notasDe2 * 2))) // 1

print(f"Notas de 5 Reais: {notasDe5}")
print(f"Notas de 2 reais: {notasDe2}")
print(f"Moedas de 1 real: {moedasDe1}")