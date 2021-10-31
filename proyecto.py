# importo el archivo csv que realice en xls
import csv
from random import choice
color_extra = ["rojo, amate" , "verde, cuidate" , "violeta, transmuta", "blanco, liberate" , "amarillo, medita"]
ruleta = choice(color_extra)
def read_csv():
    
# damos la bienvenida con una pequeña explicacion y la seleccion de colores
     print("")
print("Los colores pueden determinar tu estado de animo, asi como brindarte aquella energia que necesitas. \nEs importate que sepas, que no solo vemos los colores, sino, que los sentimos.\nPor eso antes de elegir uno, cierra los ojos unos minutos y deja que llegue a ti un color de la lista, luego colocalo en pantalla.\nPrimero completa los datos")
nombre = input("Dime tu Nombre: ")
apellido = input("Dime tu Apellido: ")
edad = input("Tu edad es: ")
print("""Ahora si elige un color de la siguiente lista 
rojo
verde
violeta
blanco
amarillo
""")

# elige un color de la lista, sino no pertenece nos avisa y debemos volver a empezar 
eleccion = input("Mi color es:")
if eleccion != ("rojo" , "verde" , "violeta" , "blanco" , "amarillo"):
     print("El color no esta en la lista, por favor reelela")

#se recorre el archivo cvs para que nos devuelva lo que seleccionamos
with open("colores.csv") as csvfile:
     data = list(csv.DictReader(csvfile, delimiter =";"))

if eleccion == "rojo":
     print(data[0] ["propiedades"])
elif eleccion == "verde":
     print(data[1] ["propiedades"])
elif eleccion == "violeta":
     print(data[2] ["propiedades"])
elif eleccion == "blanco":
     print(data[3] ["propiedades"])
elif eleccion == "amarillo":
     print(data[4] ["propiedades"])
else:
     print("Luz y Amor para tu Vida")

# al finalizar dejamos que el programa nos devuelva un color aleatorio si es que aceptamos

extra = input("Quieres recibir una recomendacion extra? Si o No ?")
if extra == "si":
     print(ruleta)
     print("Gracias por tu tiempo y vibrar conmigo")
else:
     print("Muchas gracias, hemos terminado")







if __name__ == '__main__':
     
     read_csv()
