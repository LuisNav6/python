from functools import reduce


def validacion(x):
 return x%2

def suma(x,y):
    return x+y

impares = list(filter(validacion,[1,2,3,4,5,6,7,8,9,10]))
sumaImpares = reduce(suma, impares)

print(impares)
print(f'Suma de impares:{sumaImpares}')