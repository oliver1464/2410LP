km = float(input("Quantos quilometros você quer ir? "))
passagem = km * 0.50
if km >= 200 :
    print(f"O valor da passagem foi de R${passagem * 0.45} ")
else :
    print(f"O preço da passagem foi de R${passagem} ")