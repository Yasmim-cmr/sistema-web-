def soma(a,b):
    return a + b

def subtrair(a,b):
    return a - b

def multiplicar(a,b):
    return a * b 

def dividir(a,b):
    return a / b

continuar = 1
while continuar != 0:
    print("1 Somar")
    print("2 Subtrair")
    print("3 Multiplicar")
    print("4 Dividir")
    print("0 Encerrar")

    acao = int(input("Escolha sua açao: "))
    if acao == 0:
        break
    num1 = int(input("Entre com o primeiro numero: "))
    num2 = int(input("Entre com o segundo numero: "))
    
    if acao == 1:
        result = soma(num1,num2) 
        print("Resultado ->",result)
    elif acao == 2:
        result = subtrair(num1,num2) 
        print("Resultado ->",result)
    elif acao == 3:
        result = multiplicar(num1,num2)
        print("Resultado ->",result)
    else:
        result = dividir(num1,num2)
        print("Resultado ->",result)