# Exercici 1
# L'exercici consisteix a crear un programa que et classifiqui una variable numèrica en funció l’escala Suspès/Aprovat/Notable/Excel·lent.

# Recorda que Suspès < 5, Aprovat > 5 i < 7, Notable > 7 i < 9 i Excel·lent > 9.

nota = int(input("Intruduce la nota: "))
res = ""

if nota < 5:
    res = "Suspès"
elif nota >= 5 and nota < 7:
    res = "Aprovat"
elif nota >=7 and nota < 9:
    res = "Notable"
elif nota >=9 :
    res = "Excelente"
       
           
print(res)


# - Exercici 2
# Utilitzant el següent tutorial crea un programa que et pregunti dos números. T’ha de mostrar un missatge dient si el primer és més gran, el segon és més gran o són iguals.
# ->Programiz: Python Input, Output and Import

n1 = int(input("Intruduce un numero: "))
n2 = int(input("Intruduce otro numero: "))

if n1 < n2:
    print("El numero {} es mayor que {}".format(n2,n1))
elif n1 > n2:
    print("El numero {} es mayor que {}".format(n1,n2))
else:
    print("El numero {} es igual que {}".format(n2,n1))


# - Exercici 3
# Crea un programa que et pregunti el teu nom, i et demani un número. Si el número és 0, hauria de mostrar un missatge d’error. En cas contrari, hauria de mostrar el nom repetit tants cops com indiqui el número. Per exemple, “Joan Joan Joan”.

nombre = str(input("Intruduce tu nombre: "))
num = int(input("Intruduce un numero: "))

if num == 0:
    print("Numero no válido")
else:
    print((nombre + " ") * num)


# - Exercici 4
# Crea un programa que donada una llista qualsevol, et digui si és simètrica o no. Si ho és, que et digui quants elements té.

lista = [0,1,2,3,4,5,5,4,3,2,1]
listaOp = []

for x in reversed(lista):
    listaOp.append(x)

if lista == listaOp:
    print("La lista es simetrica")
else:
    print(len(lista))

# - Exercici 5
# Crea un programa que donada una llista, et digui quants números coincideixen amb la seva posició. Per exemple [3,4,2,0,2,3,6] el 2 i el 6 coincideixen.

for x in range(len(lista)):
    if lista[x] == x:
        print("El número {} es igual a la posición {}".format(lista[x],x))