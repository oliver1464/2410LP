cigarros = int(input("Quantos cigarros você fuma por dia? "))
tempo = cigarros * 365
anos = int(input("Por quantos anos? "))
tempodevida = tempo * 10
tempodecigarro = tempodevida * anos
perda = tempodevida/24
print(f"Você perdeu {perda:.0f} de vida por causa do cigarro")
