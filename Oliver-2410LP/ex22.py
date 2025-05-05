idade = int(input("Quantos anos você tem? "))
if idade == 18 : 
    print("Você está apto a se alistar!")
if idade > 18 :
    print(f"Se passou {idade - 18} ano desde o alistamento.")
if idade < 18 :
    print(f"Faltam {18 - idade} anos para se alistar.")