c =int(input("digite su capital: "))

mes=0
intereses=0
c2=c + c
while c < c2:
    intereses = c*0.05
    c = c+intereses
    mes=mes+1
print("el capital se duplica a los " + str(mes) + "meses")