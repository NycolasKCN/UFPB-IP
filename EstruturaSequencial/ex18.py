"""Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade 
de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo
usando este link (em minutos)."""

tamanho_arquivo = float(input("Digite o tamanho do arquivo: (em MB) "))
velocidade_download = float(input("Digite a velocidade de download: (em Mbps) "))

tempo_em_sec = tamanho_arquivo / velocidade_download # tempo recebe o tempo de download em segundos
tempo_em_minutos = tempo_em_sec / 60

print(f"O download será efetuado em {tempo_em_minutos:.1f} minutos")
