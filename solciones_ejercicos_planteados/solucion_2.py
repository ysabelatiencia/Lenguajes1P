print("PROBLEMA 1")
nota=14;
if(nota>18):
    print("BECA CONCEDIDA")
elif(nota<=18 and nota>=15):
    print("POSIBLE APELACION")
elif(nota<15):
    print("BECA DENEGADA")

print("PROBLEMA 2")
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

print("PROBLEMA 3")
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

print("PROBLEMA 4")
est_entregaron_tarea=30
est_no_entregaron_tarea=9

if(est_no_entregaron_tarea<10 and est_entregaron_tarea>30):
    print("GRADO DE EFICIENCIA 9")
else:
    if(est_no_entregaron_tarea<10):
        print("GRADO DE EFICIENCIA 5")
    if(est_entregaron_tarea>30):
        print("GRADO DE EFICIENCIA 7")

print("PROBLEMA 5")
materias=int(input("Ingrese su numero de materias"))
credito=int(input("Ingrese su numero de creditos"))

if((materias>=4 and materias<=6) or (credito>11)):
    print("Estudiante Regular")
else:
    print("Estudiante Irregular")

print("PROBLEMA 6")
A={"Isabel":9,"Juan":6,"Fernando":5,"Elias":4,"Simon":2,"Felipe":1,"Luisa":7,"Maria":8,"Renata":3,"Ana":2}
for nombre,promedio in A.items():
    if(promedio>8):
        print("BECA CONCEDIDA a" +nombre+" Promedio"+str(promedio))
    elif(promedio<5):
        print("BECA DENEGADA a"+nombre+" Promedio"+str(promedio))
    else:
        print("POSIBLE APELACION a"+nombre+" Promedio"+str(promedio))

print("PROBLEMA 7")
edad=20
cantidad_consumida=22.3

print("PROBLEMA 8")
def promedio(notas):
    promedio=0
    for nota in notas:
        promedio+=nota
    return (promedio/len(notas))
def condicional(promedio):
    if(promedio>8):
        print("BECA CONCEDIDA")
    else:
        print("BECA DENEGADA")

e={"Isabel":[10,9,9],"Juan":[8,6,7],"Fernando":[9,5,4],"Elias":[8,9,4],"Simon":[4,5,7],"Felipe":[8,2,3],"Luisa":[10,10,5],"Maria":[9,6,8],"Renata":[2,4,5],"Ana":[8,9,7]}
for estudiante,notas in e.items():
    print("Estudiante "+ estudiante)
    condicional(promedio(notas));
print("PROBLEMA 9")
a=True#ON
b=True#MENOR 30°
c=False#ABIERTA

if(not c):
    print("Sistema Apagado")
else:
    if(b):
        print("Sistema Encendido")
    if(a):
        print("Sistema Encendido")
print("PROBLEMA 10")
n1=int(input("Numero 1: "))
n2=int(input("Numero 2: "))
n3=int(input("Numero 3: "))

if(n1<n2 and n1<n3):
    print(n1)
    if(n2<n3):
        print(n2)
        print(n3)
    else:
        print(n3)
        print(n2)
if(n2<n1 and n2<n3):
    print(n2)
    if(n1<n3):
        print(n1)
        print(n3)
    else:
        print(n3)
        print(n1)
if(n3<n1 and n3<n2):
    print(n3)
    if(n2<n1):
        print(n2)
        print(n1)
    else:
        print(n1)
        print(n2)
