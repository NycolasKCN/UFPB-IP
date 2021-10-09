"""Sheldon tem uma grande coleção de revistas em quadrinhos raras e resolveu doá-las a seus amigos (Bazinga!!!). 
Escreva um programa que receba como entrada a quantidade total de revistas e a quantidade de amigos que serão beneficiados, 
e exiba quantas revistas cada um vai receber e quantas sobrarão para Sheldon."""

totalRevistas = int(input("Digite a quantidade total de revistas: "))
totalAmigos = int(input("Digite a quantidade total de amigos: "))

revistasParaAmigos = totalRevistas // totalAmigos
revistasParaSheldon = totalRevistas % totalAmigos

print(f"Sheldon tinha {totalRevistas} revistas e {totalAmigos} amigos")
print(f"Cada amigo recebeu {revistasParaAmigos} revistas.")
print(f"Sheldon ficou com {revistasParaSheldon}")