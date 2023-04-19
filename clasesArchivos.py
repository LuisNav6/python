import pickle as p
class vehiculo:
    #inicializamos objeto/constructor
    def __init__(self,ruedas,puertas,color):
        self.ruedas = ruedas
        self.puertas = puertas
        self.color = color
    #sobrescribimos el metodo __str__ con el formateo 
    def __str__ (self):
        return f'{self.ruedas} {self.puertas} {self.color}'
#creamos el objeto   
v = vehiculo(4,4,"blanco")
#guardamos el objeto
with open ('vehiculos.pickle',"wb") as arch:
    p.dump(v, arch)
#cargamos el objeto desde el archivo 
with open('vehiculos.pickle',"rb") as arch:
    vCargado = p.load(arch)
#imprimimos lo que tiene el archivo 
print(f"tiene {vCargado.ruedas} ruedas, {vCargado.puertas} puertas y es de color {vCargado.color}")
