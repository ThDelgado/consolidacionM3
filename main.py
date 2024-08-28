#creando la lista

mi_lista = [
 "Harry Houdini",
 "Newton", 
 "David Blaine", 
 "Hawking", 
 "Messi", 
 "Teller", 
 "Einstein",  
 "Pele",  
 "Juanes", 
]

#clasificando los personajes
from funciones import seleccion

magos = seleccion.mago_clasificar(mi_lista)
cientifico = seleccion.cientifico_clasificar(mi_lista)
otro = seleccion.otro_clasificar(mi_lista)


#obteniendo los magos grandiosos
from funciones import utiles

magos = seleccion.mago_clasificar(mi_lista)
magos_grandiosos = utiles.hacer_grandioso(magos)

#funcion de impresion
def imprimir_nombres(lista):
    print(lista)
    return

#respuestas de funciones
print("Los magos grandiosos son: ")
imprimir_nombres(magos_grandiosos)
print()
print("Los magos son: ")
imprimir_nombres(magos)
print()
print("Los cientificos son: ")
imprimir_nombres(cientifico)
print()
print("Entre otros personajes tenemos: ")
imprimir_nombres(otro)

