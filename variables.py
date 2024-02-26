#Aprendamos sobre variables
#El lado izquierdo de la variable se conoce como identificador, el sìmbolo en la mitad (=) se conoce como sìmbolo de asignaciòn y
#me asigna al espacio de memoria identificado con el nombre de la variable el valor que se encuentra a la derecha
x = 20

#Tenemos los tipos de datos, string, integer, float, and bool. Estos se conocen como
#Tipo de dato de dato primario

nombre = 'Santiago' #Esto es un str
edad = 20 #Es un tipo de dato Integer Int
estatura = 1.99 #Es un tipo Float
is_profesor = True #Es tipo bool (False)

apellido = 'Echeverri'

nombre_completo = nombre + ' ' + apellido

Listas = [1,'valor',3,False,4,5.6 ] #Las listas son mutables

Listas[0]= 2

tuplas = (1,'valor', 3 , True, 2.1) #Las tuplas son inmutables


for value in tuplas:
    print(value)