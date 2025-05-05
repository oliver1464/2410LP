import time
a = float(input("Me diga um numero A: "))
b = float(input("Me diga outro numero B: "))
c = float(input("Me diga mais um numero C: "))
delta = (b ** 2) + ((- 4 * a )* c)
print("Para calcular o Delta precisamos fazer B^2-4.A.C ")
print("Aguarde 1.5 segundos...")
time.sleep(1.5)
print(f"O valor de delta é: {delta} ")

