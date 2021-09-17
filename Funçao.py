def sumDigitos():
    """ Soma os digitos de uma sting e printa o resultado
    return: None"""
    listaStr = list()
    soma = 0
    numeros = str(input("Digite os numeros entre 1000 e 9999: "))
    numerosInt = int(numeros)
    if 1000 <= numerosInt <= 9999:
        for digitos in range(len(numeros)):
            listaStr.append(numeros[digitos])
        for item in listaStr:
            soma = soma + int(item)
        print(f"O resultado da soma dos digitos é: {soma}")
    else:
        print("Valor digitado é invalido")
   

sumDigitos()