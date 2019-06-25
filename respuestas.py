print("1")
nota=14;
if(nota>18):
    print("BECA CONCEDIDA")
elif(nota<=18 and nota>=15):
    print("POSIBLE APELACION")
elif(nota<15):
    print("BECA DENEGADA")

print("2")
peso=121
if(peso<=120):
    print("DESNUTRIDO\n")
    print("NIVEL\n")
    if(peso<80):
        print("DESNUTRICION ||")
    else:
        print("DESNUTRICION |")
elif(peso>=180):
    print("OBESIDAD")
    if(peso>180 and peso<200):
        print("OBESIDAD |")
    else:
        print("OBESIDAD ||")
elif(peso>=121 and peso<=179):
    print("PESO IDEAL")

print("3")
cantidad=float(input("INGRESE CANTIDAD "))
if(cantidad>0 and cantidad<=5):
    descuento=10
if(cantidad>5 and cantidad<=10):
    descuento = 20
if(cantidad>10 and cantidad<=20):
    descuento = 30
if(cantidad>20):
    descuento=45
print("DESCUENTO="+str(descuento)+"%")

print("4")
