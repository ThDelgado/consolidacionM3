#funcion clasificando magos
def mago_clasificar(mi_lista):
    mago = []
    for magos in mi_lista:
        if magos == "Harry Houdini":
            mago.append(magos)  
        elif magos == "David Blaine":
            mago.append(magos)
        elif magos == "Teller":
            mago.append(magos)
    return mago

#funcion clasificacion cientificos
def cientifico_clasificar(mi_lista): 
    cientifico = []
    for cientificos in mi_lista:
        if cientificos == "Newton":
            cientifico.append(cientificos)
        if cientificos == "Hawking":
            cientifico.append(cientificos)
        if cientificos == "Einstein":
            cientifico.append(cientificos)
    return cientifico


#funcion clasificacion de otros personajes
def otro_clasificar(mi_lista):
    otro = []
    for otros in mi_lista:
        if otros == "Messi":
            otro.append(otros)
        elif otros == "Pele":
            otro.append(otros)
        elif otros == "Juanes":
            otro.append(otros)

    return otro