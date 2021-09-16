def sumDigitos():
    """
    return: None"""
    listaStr = list()
    soma = 0
    numeros = str(input("Digite os numeros entre 1000 e 9999: "))
    if len(numeros) == 4:
        for digitos in range(len(numeros)):
            listaStr.append(numeros[digitos])
        for item in listaStr:
            soma = soma + int(item)
        print(f"O resultado da soma dos digitos é: {soma}")
    else:
        print("Valor digitado é invalido")
   

sumDigitos()