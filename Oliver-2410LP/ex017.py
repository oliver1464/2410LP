velocidade = float(input("Qual velocidade do carro? "))
multa = velocidade * 5
if  velocidade >= 80:
    print(f"Você foi multado! o valor da multa é R${multa} ")
else:
    print("Ok tudo certo.")