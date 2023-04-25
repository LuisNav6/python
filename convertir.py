"""
autor: Luis Navarrete.
El ejercicio evalua que el parametro a tiene que ser igual a el parametro b
esto solo mediante la capitalizacion y la eliminacion de caracteres
si es posible entonces retorna que si.
Es importante que la longitud de a no sea menor que la longitud de b

Lo que se hace es crear una matriz de boleanos, la cual se inicializa en false
conforme se va validando las posiciones de cada parametro acorde a las condiciones dadas
el estado de la casilla de la matriz de x+1 * y+1 se ira actualizando segun sea el caso

"""
def convertir(a, b):
    x = len(a)
    y = len(b)
    table = [[False] * (y+1) for _ in range(x+1)]
    table[0][0] = True
    for i in range(x+1):
        for j in range(y+1):
            if table[i][j]:
                if j < y and i < x and a[i].upper() == b[j]:
                    table[i+1][j+1] = True
                if i < len(a) and a[i].islower():
                    table[i+1][j] = True
    return f"Si es posible" if table[x][y] else f"No es posible"


b = input(str("Dame la cadena a igualar:"))
a = input(str("Dame la cadena que quieres que iguale:"))

print(f'Dado a como: {a} y b como: {b} el resultado de la evaluación es: {convertir(a,b)}')


      

    
             
                 
                 