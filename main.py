

print("Calculemos tu IMC ")

peso = float(input("ingresa tu peso en kilos "))
altura = float(input("ingresa tu altura en metros "))

IMC =  peso / (altura * altura)
 
roundIMC = round(IMC, 2)

print("Tu IMC es: ", roundIMC)

