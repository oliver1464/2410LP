import time
produto = float(input("Me diga o preço do produto R$"))
desconto = produto * 0.05
print("Com 5% de desconto o seu produto ficara ")
for i in range(5):
    print(f"Pensando: {i}")
    time.sleep(1)
print(f"R${produto - desconto}")