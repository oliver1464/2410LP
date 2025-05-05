print("Saiba se é um triangulo...")
a = float(input("Primeira reta valor:"))
b = float(input("Segunda reta valor:"))
h = float(input("Terceira reta valor:"))
if b < a + h and a < b + h and h < a + b :
    print("É um triangulo!")
else : 
    print("Não é um triangulo!")