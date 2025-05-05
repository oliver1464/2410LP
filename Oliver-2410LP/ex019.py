nome = input("Qual eo nome do aluno? ")
nota1 = float(input("Qual ea primeira nota do aluno? "))
nota2 = float(input("Qual ea segunda nota do aluno? "))
resultado = (nota1 + nota2)/2
if resultado >= 7.0 :
    print(f"O {nome} teve uma média de {resultado} foi um bom aproveitamento!")
else :
    print(f"O {nome} teve uma média de {resultado} foi um mau aproveitamento")
