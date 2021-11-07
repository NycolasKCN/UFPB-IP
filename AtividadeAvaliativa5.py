"""Escreva um programa em python que tenha uma lista chamada familia e inicialize com o nome de 10 parentes seus 
(pais, primos, tios, avós). Depois escreva os seguintes comandos: 1- com a função append() , escreva o nome de 
algum animal de estimação da família (invente um nome se não tiver); 2 - remova a pessoa do índice 2 da sua lista; 
3 - substitua a pessoa do índice 4 por outro membro da sua família; 4 - escreva o comando que coloca sua lista em 
ordem alfabética (dica: pesquise o noma da função). """
from os import system as sys

sys("cls")

familia = ["nycolas", "mariah", "yanni", "joselia",
           "junior", "livia", "joão", "cauã", "rafael", "marcio"]
print("Alguns membros da minha familia")
print(familia, "\n")

# Comando 1
# Adicionando o nome do animal de estimação
familia.append("ametista")
print("Está é a lista após adicionar o animal.")
print(familia, "\n")

# Comando 2
# Removendo a pesso do índice 2
familia.pop(2)
print("Está é a lista após remover a pessoa do índice dois")
print(familia, "\n")

# Comando 3
# Substituindo a pessoa do índice 4
familia[4] = "sinara"
print("Está é a lista com a substituição")
print(familia, "\n")

# Comando 4
# Colocando a lista em ordem alfabética
familia.sort()
print("E está é a lista em ordem alfabética")
print(familia)
