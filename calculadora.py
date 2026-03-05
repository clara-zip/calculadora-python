print ("Calculadora")

num1 = int(input("Digite o primeiro número:"))

operador = input("Digite a opção desejada (1 para soma, 2 para subtração, 3 para divisão e 4 para multiplicação):")

num2 = int(input("Digite o segundo número:"))

if operador == "1":
    operação = num1 + num2
elif operador == "2":
    operação = num1 - num2
elif operador == "3":
    operação = num1 / num2
elif operador == "4":
    operação = num1 * num2
else:
    operação = "Operador Inválido, Use: 1, 2, 3 ou 4."
print ("Resultado:")
print (operação)





