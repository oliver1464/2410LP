print(f"Bom dia!, estamos fazendo uma promoção em nossa loja de 5% de desconto para homens e 13% de desconto para mulheres, por favor digite")
nome = input("nome: ")
sexo = input("sexo: ")
valor = float(input("Quanto gastou R$"))
if sexo == 'Homem' :
    print(f"Sr.{nome} você gastou R${valor} em nossa loja então você tera R${valor * 0.05} de desconto!")
if sexo == 'Mulher' :
    print(f"Sra.{nome} você gastou R${valor} em nossANgea loja então você tera R${valor * 0.13} de desconto!")