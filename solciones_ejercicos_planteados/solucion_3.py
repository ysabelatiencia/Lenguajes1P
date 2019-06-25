'''Realice en código un programa en donde tenga una variable de tipo entera,
que contenga la nota de una de las materias que vio. Si la nota de esa materia
es mayor a 18 mostrará por pantalla “BECA CONCEDIDA”, si es menor que 15 mostrará
por pantalla “BECA DENEGADA” caso contrario imprimirá “POSIBLE APELACION”.'''

def Ejercicio1():
    var=10
    if(var>18):
        print(" BECA CONCEDIDA")
    elif (var<15):
        print("BECA DENEGADA")
    else:
        print("POSIBLE APELACIÓN")

'''Realice en código un programa en Python en donde con el peso se identificará si se encuentra DESNUTRIDO, PESO IDEAL U OBESO. 
Si su peso es menor que 120, se encontrará en el nivel de DESNUTRIDO (el cual debe ser mostrado por pantalla) en donde deberá 
verificar cual es el nivel de DESNUTRICION que posee, si su peso es menor a 80 posee DESNUTRICION II y si es menor a 120 y mayor 
a 80 posee DESNUTRICION I. (El subnivel también debe ser mostrado por pantalla)
Si su peso es mayor a 180, se encontrará en el nivel de OBESIDAD (el cual debe ser mostrado por pantalla) en donde deberá 
verificar el nivel de OBESIDAD que posee, si su peso es mayor a 180 y menor a 200 posee OBESIDAD I y si es mayor a 
200 posee OBESIDAD II. (El subnivel también debe ser mostrado por pantalla)
Si su peso se encuentra entre 121 y 179, indicará que su peso es ideal.
'''

def Ejercicio2():
    peso=80
    if(peso<120):
        print("DESNUTRIDO")
        if(peso<80):
            print("DESNUTRICIÓN II")
        else:
            print("DESNUTRICIÓN I")
    elif(peso>180):
        print("OBESIDAD")
        if (peso >200):
            print("OBESIDAD II")
        else:
            print("OBESIDAD I")
    else:
        print("PESO IDEAL")


''' En una carnicería se ofrece descuento en la compra según la cantidad que adquiera. 
Si la cantidad comprada se encuentra entre 0-5kg obtiene un descuento del 10%; 
si se encuentra entre 5.01-10kg obtiene un descuento del 20%; si se encuentra entre 10.01-20kg 
obtiene un descuento del 30% y si es mayor a 20Kg el descuento es del 45%. 
Muestre el descuento que se le realiza por una compra específica.
NOTA: Los datos de la cantidad comprada es ingresada por consola y además no puede hacer uso de ELIF
'''

def Ejercicio3():
    cantidad=input("Ingrese cantidad: ")
    if(cantidad>=0 and cantidad <5):
        print("Su descuento es de 10%")
    if(cantidad>=5.01 and cantidad <10):
        print("Su descuento es de 20%")
    if(cantidad>=10.01 and cantidad <20):
        print("Su descuento es de 30%")
    if(cantidad >20):
        print("Su descuento es de 45%")

'''Se desea calcular el nivel de eficiencia de un curso de matemáticas, de acuerdo con las siguientes 
condiciones que se testean en un tiempo de prueba.
	Menos de 10 estudiantes no entregaron la tarea.
	Mas de 30 estudiantes entregaron la tarea.
	La eficiencia se calcula de la siguiente manera:
	Si solo cumple la primera condición, su grado de eficiencia es de 5.
	Si solo cumple la segunda condición, su grado de eficiencia es de 7.
	Si cumple ambas condiciones, su grado de eficiencia es de 9.
NOTA: NO USAR ELIF
'''
def Ejercicio4():
    estudiantes=input("Ingrese los estudiantes que han entregado la tarea: ")
    if(estudiantes<10):
        print("EFICIENCIA 5")
    if(estudiantes>30):
        print("EFICIENCIA 7")
    if(estudiantes>10 and estudiantes<30):
        print("EFICIENCIA 9")


'''  Validar que cada estudiante de ESPOL que este cursando en al menos 4 y a lo mucho 
6 materias o posea un número de créditos mayor a 11 se considere “Estudiante regular”, 
caso contrario “Estudiante irregular”. El estudiante debe ingresar la cantidad de materias 
que cursa y la cantidad de créditos.'''
def Ejercicio5():
    materias=input("Ingrese las materias que esta cursando: ")
    creditos=input("Ingrese el numero de creditos")
    if(materias>=4 and materias<=6):
        if(creditos>11):
            print("ESTUDIANTE REGULAR")
        else:
            print("Estudiante irregular")
    else:
        print("Estudiante irregular")

'''   Si un grupo de estudiantes con promedio:
A={‘Isabel’:9,’Juan’:6,’Fernando’:5,’Elias’:4,’Simon’:2,’Felipe’:1,’Luisa’:7,’Maria’:8,’Renata’:3,’Ana’:2}
Realice un código en donde los promedios (sobre 10) se verifique si es apto para adquirir una beca universitaria. 
Si el promedio de esas materias es mayor a 8 mostrara por pantalla “BECA CONCEDIDA”, 
si es menor que 5 mostrara por pantalla “BECA DENEGADA” caso contrario imprimirá “POSIBLE APELACION”.
'''
def Ejercicio6():
    A={"Isabel":9,"Juan":6,"Fernando":5,"Elias":4,"Simon":2,"Felipe":1,"Luisa":7,"Maria":8,"Renata":3,"Ana":2}
    for estudiante in A:
        if (A[estudiante] > 18):
            print(estudiante+" BECA CONCEDIDA")
        elif (A[estudiante]  < 15):
            print(estudiante+" BECA DENEGADA")
        else:
            print(estudiante+" POSIBLE APELACIÓN")

'''  Se quiere determinar si una persona tiene probabilidad alta o baja de tener colesterol elevado. 
Para eso se usa la EDAD y CANTIDAD CONSUMIDA EN GRAMOS. Si la persona se encuentra con un consumo bajo, 
tendrá una probabilidad baja de tener colesterol elevado. La siguiente tabla es de referencia para las 
cantidades designadas según la edad. Asigne el valor ‘1’ si la persona posee probabilidad alta y ‘0’ si la
 persona tiene la probabilidad baja de tener colesterol elevado.
EDAD			KG de grasa
0-1	Mes		10g – 20g
>1 - <=6 meses		15g – 25g
>6 - <=12 meses	25g – 45g
>1 - <=5anos		35g – 50g
>5-10 anos		45g – 70g
'''
def Ejercicio7():
    edad = input("Ingrese su edad: ")
    grasa= input("Ingrese la cantidad consumida en gramos:")
    probabilidad=0
    if(edad>=0 and edad <=1 and grasa>10 and grasa <20):
        probabilidad=0
    elif(edad>1 and edad <=6 and grasa>15 and grasa <25):
        probabilidad=0
    elif (edad > 6 and edad <= 12 and grasa > 25 and grasa < 45):
        probabilidad = 0
    elif (edad > 12 and edad <= 60 and grasa > 35 and grasa < 50):
        probabilidad = 0
    elif (edad > 60 and edad <= 120 and grasa > 45 and grasa < 70):
        probabilidad = 0
    else:
        probabilidad=1
    return probabilidad

''' Si un grupo de estudiantes con notas de la materia Física 
e={‘Isabel’:[10,9,9],’Juan’:[8,6,7],’Fernando’:[9,5,4],’Elias’:[8,9,4],
’Simon’:[4,5,7],’Felipe’:[8,2,3],’Luisa’:[10,10,5],’Maria’:[9,6,8],’Renata’:[2,4,5],’Ana’:[8,9,7]}
realice una función que calcule los promedio (sobre 10) y otra función que devuelva verdadero en 
caso de que el promedio de esas materias es mayor a 8 y se muestre por pantalla “BECA CONCEDIDA” a
 x alumno, si es menor que 5 se mostrara por pantalla “BECA DENEGADA” a x alumno y retornara falso.
'''

def Ejercicio8():
    E = {"Isabel":[10, 9, 9],"Juan":[8, 6, 7],"Fernando":[9, 5, 4],"Elias":[8, 9, 4],
         "Simon":[4, 5, 7],"Felipe":[8, 2, 3],"Luisa":[10, 10, 5],"Maria":[9, 6, 8],"Renata":[2, 4, 5],"Ana":[8, 9, 7]}
    Becas(CalcularPromedio(E))

def CalcularPromedio(E):
    Promedios={}
    for estudiante in E:
        promedio=E[estudiante].sum()/3
        Promedios[estudiante]=promedio
    return Promedios

def Becas(Promedios):
    for estudiante in Promedios:
        if(Promedios[estudiante]>8):
            print(estudiante+ ": BECA CONCEDIDA")
        elif(Promedios[estudiante]<5):
            print(estudiante+": BECA DENEGADA")
        else:
            return False
    return True

''' Un sistema de A.C. se puede poner en marcha por un interruptor manual “a” (on|off/true|false). 
Se encenderá de forma automática, aunque el interruptor esté en off cuando el termóstato “b” detecte
 que la temperatura exterior pasa los 30°C. Finalmente se posee un detector “c” que apaga el sistema
  cuando la ventana esta abierta. Diseñe las condiciones en un instante de tiempo.'''
def Ejercicio9(a,b,c):
    if(c==0):
        print("SISTEMA OFF")
    elif(b==1):
        print("SISTEMA ON")
    elif(a==1):
        print("SISTEMA ON")
    else:
        print("SISTEMA OFF")

'''Pedir por pantalla 3 números enteros y mostrarlos ordenados de menor a mayor.  '''
def Ejercicio10():
    a=input("Ingrese el 1° número: ")
    b = input("Ingrese el 2° número: ")
    c = input("Ingrese el 3° número: ")
    if(a>=b and a>=c):
        if(b>=c):
            print(a+"  "+b+" "+c)
        else:
            print(a + "  " + c + " " + b)
    elif (b >= a and b >= c):
        if (a >= c):
            print(b + "  " + a + " " + c)
        else:
            print(b+ "  " + c + " " + a)
    elif (c >= a and c >= b):
        if (a >= b):
            print(c + "  " + a + " " + b)
        else:
            print(c+ "  " + b + " " + a)