'''
1.  Realice en código un programa en donde tenga una variable de tipo entera, que contenga la nota de una de las materias que vio.
 Si la nota de esa materia es mayor a 18 mostrará por pantalla “BECA CONCEDIDA”, si es menor que 15 mostrará por pantalla “BECA DENEGADA”
 caso contrario imprimirá “POSIBLE APELACION”.
'''

print("SOLUCION NIVEL 1")
nota = 17

if nota > 18:
    print("BECA CONCEDIDA")
elif nota <15:
    print("BECA DENEGADA")
else:
    print("POSIBLE APELACION")


'''
2. Realice en código un programa en Python en donde con el peso se identificará si se encuentra DESNUTRIDO, PESO IDEAL U OBESO. 
Si su peso es menor que 120, se encontrará en el nivel de DESNUTRIDO (el cual debe ser mostrado por pantalla) en donde deberá verificar 
cual es el nivel de DESNUTRICION que posee, si su peso es menor a 80 posee DESNUTRICION II y si es menor a 120 y mayor a 80 posee DESNUTRICION I. 
(El subnivel también debe ser mostrado por pantalla)
Si su peso es mayor a 180, se encontrará en el nivel de OBESIDAD (el cual debe ser mostrado por pantalla) en donde deberá verificar el nivel 
de OBESIDAD que posee, si su peso es mayor a 180 y menor a 200 posee OBESIDAD I y si es mayor a 200 posee OBESIDAD II. 
(El subnivel también debe ser mostrado por pantalla)
Si su peso se encuentra entre 121 y 179, indicará que su peso es ideal.
'''

print("SOLUCION NIVEL 2")

peso = 175

if peso <120:
    print("Se encuentra en nivel de DESNUTRIDO")
    if peso<80:
        print("NIVEL II")
    else:
        print("NIVEL I")
elif peso>180:
    print("Se encuentra en nivel de OBESIDAD")
    if 180>peso>200:
        print("NIVEL I")
    else:
        print("NIVEL II")
elif 121>peso>179:
    print("PESO IDEAL")

'''
3.  En una carnicería se ofrece descuento en la compra según la cantidad que adquiera. Si la cantidad comprada se encuentra 
entre 0-5kg obtiene un descuento del 10%; si se encuentra entre 5.01-10kg obtiene un descuento del 20%; si se encuentra entre 10.01-20kg 
obtiene un descuento del 30% y si es mayor a 20Kg el descuento es del 45%. Muestre el descuento que se le realiza por una compra específica.
NOTA: Los datos de la cantidad comprada es ingresada por consola y además no puede hacer uso de ELIF
'''

cantidad_comprada = 8.00
resultado=0
if 0>cantidad_comprada>5:
    print("El descuento es " ,(cantidad_comprada*0.1))
if 5.01>cantidad_comprada>10:
    print("El descuento es ", (cantidad_comprada * 0.2))
if 10.01>cantidad_comprada>20:
    print("El descuento es ", (cantidad_comprada * 0.3))
if cantidad_comprada>20.01:
    print("El descuento es ", (cantidad_comprada * 0.4))

'''
4.Se desea calcular el nivel de eficiencia de un curso de matemáticas, de acuerdo con las siguientes condiciones que se testean en un 
tiempo de prueba.
	Menos de 10 estudiantes no entregaron la tarea.
	Mas de 30 estudiantes entregaron la tarea.
	La eficiencia se calcula de la siguiente manera:
	Si solo cumple la primera condición, su grado de eficiencia es de 5.
	Si solo cumple la segunda condición, su grado de eficiencia es de 7.
	Si cumple ambas condiciones, su grado de eficiencia es de 9.
NOTA: NO USAR ELIF
'''


no_entragan_tarea = 20
entragan_tarea = 10

if no_entragan_tarea<10 and entragan_tarea>30:
    print("Eficiencia es de 9")
if no_entragan_tarea<10:
    print("Eficiencia es de 5")
if entragan_tarea>30:
    print("Eficiencia es de 7")



'''
5. Validar que cada estudiante de ESPOL que este cursando en al menos 4 y a lo mucho 6 materias o posea un número de créditos mayor a 11 
se considere “Estudiante regular”, caso contrario “Estudiante irregular”. El estudiante debe ingresar la cantidad de materias que cursa
 y la cantidad de créditos.

'''

numero_materias = 5
numero_creditos= 15

if 4>=numero_materias>6 or numero_creditos>11:
    print("Es estudiante regular")
else:
    print("Es estudiante irregular")


'''
6. Si un grupo de estudiantes con promedio:
A={‘Isabel’:9,’Juan’:6,’Fernando’:5,’Elias’:4,’Simon’:2,’Felipe’:1,’Luisa’:7,’Maria’:8,’Renata’:3,’Ana’:2}
Realice un código en donde los promedios (sobre 10) se verifique si es apto para adquirir una beca universitaria. 
Si el promedio de esas materias es mayor a 8 mostrara por pantalla “BECA CONCEDIDA”, si es menor que 5 mostrara por pantalla 
“BECA DENEGADA” caso contrario imprimirá “POSIBLE APELACION”.

'''

Alumnos={'Isabel':9,'Juan':6,'Fernando':5,'Elias':4,'Simon':2,'Felipe':1,'Luisa':7,'Maria':8,'Renata':3,'Ana':2}

lista_alumnos = list(Alumnos.keys())
for alumno in lista_alumnos:
    if Alumnos[alumno] >8:
        print("El alumno ",alumno+" se la otorgado la beca")
    elif Alumnos[alumno] <5:
        print("El alumno ", alumno + " se la denegado la beca")
    else:
        print("El alumno ", alumno + " puede apelar a la beca")


'''
7.Se quiere determinar si una persona tiene probabilidad alta o baja de tener colesterol elevado. Para eso se usa la EDAD y CANTIDAD CONSUMIDA 
EN GRAMOS. Si la persona se encuentra con un consumo bajo, tendrá una probabilidad baja de tener colesterol elevado. La siguiente tabla es 
de referencia para las cantidades designadas según la edad. Asigne el valor ‘1’ si la persona posee probabilidad alta y ‘0’ si la persona 
tiene la probabilidad baja de tener colesterol elevado.
EDAD			KG de grasa
0-1`Mes		10g – 20g
>1 - <=6 meses		15g – 25g
>6 - <=12 meses	25g – 45g
>1 - <=5anos		35g – 50g
>5-10 anos		45g – 70g
'''

edad_anual = 22
edad_mes = 22*12
consumo = 30

probabilidad = 0

if 0<edad_mes<1 and consumo<20:
    probabilidad = 0
else:
    probabilidad =1

if 1.01<edad_mes<=6 and consumo<25:
    probabilidad = 0
else:
    probabilidad =1

if 6.01<edad_mes<12 and consumo<45:
    probabilidad = 0
else:
    probabilidad =1

if 12.01<edad_mes<(12*5) and consumo<50:
    probabilidad = 0
else:
    probabilidad =1

if edad_mes>(12.01*5) and consumo<70:
    probabilidad = 0
else:
    probabilidad =1

if probabilidad ==0:
    print("Su probabilidad de tener colesterol alto, es baja")
else:
    print("Su probabilidad tener colesterol alto, es alta")


'''
8.Si un grupo de estudiantes con notas de la materia Física 
e={‘Isabel’:[10,9,9],’Juan’:[8,6,7],’Fernando’:[9,5,4],’Elias’:[8,9,4],’Simon’:[4,5,7],’Felipe’:[8,2,3],
’Luisa’:[10,10,5],’Maria’:[9,6,8],’Renata’:[2,4,5],’Ana’:[8,9,7]}
realice una función que calcule los promedio (sobre 10) y otra función que devuelva verdadero en caso de que el promedio de esas 
materias es mayor a 8 y se muestre por pantalla “BECA CONCEDIDA” a x alumno, si es menor que 5 se mostrara por pantalla “BECA DENEGADA” a x 
alumno y retornara falso.
'''


def promedio(lista_notas):
    #print(sum(lista_notas)/len(lista_notas))
    return sum(lista_notas)/len(lista_notas)


def beca_con_promedio(promedio):
    #print(promedio)
    if promedio > 8:
        print("BECA CONCEDIDA")
        return True
    elif 5<promedio<8:
        print("BECA CONSIDERADA")
        return False
    else:
        print("BECA DENEGADA")
        return False

estudiantes={'Isabel':[10,9,9],'Juan':[8,6,7],'Fernando':[9,5,4],'Elias':[8,9,4],'Simon':[4,5,7],'Felipe':[8,2,3],'Luisa':[10,10,5],
             'Maria':[9,6,8],'Renata':[2,4,5],'Ana':[8,9,7]}


lista_de_estudiantes = list(estudiantes.keys())

for estudiante in lista_de_estudiantes:
    print("El/La alumn@ ",estudiante+" tiene ",)
    beca_con_promedio(promedio(estudiantes[estudiante]))


'''
9.Un sistema de A.C. se puede poner en marcha por un interruptor manual “a” (on|off/true|false). Se encenderá de forma automática, 
aunque el interruptor esté en off cuando el termóstato “b” detecte que la temperatura exterior pasa los 30°C. 
Finalmente se posee un detector “c” que apaga el sistema cuando la ventana esta abierta. Diseñe las condiciones en un instante de tiempo.
'''


temperaturaB=35
ventana =1
manual = False;

if temperaturaB>30 or manual:
    if ventana==1:
        print("sistema ON")
    else:
        print("Sistema OFF")
elif temperaturaB<30 or manual:
    if ventana == 1:
        print("sistema ON")
    else:
        print("Sistema OFF")









'''
Pedir por pantalla 3 números enteros y mostrarlos ordenados de menor a mayor.
'''

print("Ingrese 3 numeros: ")
print("Numero 1: ")
a= int(input())
print("Numero 2: ")
b= int(input())
print("Numero 1: ")
c= int(input())

#a,b,c
#a,c,b
#b,a,c
#b,c,a
#c,a,b
#c,b,a


if a>b and a>c:
    if b>c:
        print(c,",",b,",",a)
    else:
        print(b,",",c,",",a)
elif b>a and b>c:
    if c>a:
        print(a,",",c,",",b)
    else:
        print(c,",",a,",",b)
elif c>a and c>b:
    if b>a:
        print(a,",",b,",",c)
    else:
        print(b,",",a,",",c)


