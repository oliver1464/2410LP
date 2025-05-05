idade = int(input("Quantos anos você tem? "))

if(idade <= -1):
      print("Você não nasceu ainda!!!")
elif( idade >= 0 and idade <= 4 ):
    print("Você é um bebe.")
    pass
elif idade >= 5 and idade <= 12 :
        print("Você é uma criança.")
        pass
elif idade >= 13 and idade <= 18 :
      print("Você é um adolescente.")
      pass
elif idade >= 19 and idade <= 29 :
      print("Você é um jovem adulto.")
      pass
elif idade >= 30 and idade <= 59 :
      print("Você é um adulto.")
      pass
elif(idade >= 60 and idade <= 120):
      print("Você é uma pessoa idosa.")
      pass
else:
      print("Você está em uma idade AVANÇADA!!!!")
      pass