"""
Contiene el metodo para que la salida cuando se repiten condimentos sea double triple o nx.
"""

def pretty_print( description) -> str:
    """
    Función útil para formatear la descripción de la bebida y sus condimentos.
    """
    lista = description.split(", ")
    unicos= list(dict.fromkeys(lista[1:]))
    texto = lista[0]
    for i in unicos:
        cant = lista.count(i)
        if cant == 1:
            texto= texto + ", "+ i
        elif cant == 2:
            texto= texto + ", Double "+i
        elif cant == 3:
            texto= texto + ", Triple "+i
        else:
            texto= texto + ", "+ str(cant)+"x "+i
    return texto 
