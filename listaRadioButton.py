import tkinter as tk

root = tk.Tk()
root.title("Lista de opciones")

# Crear objeto IntVar para controlar la opción seleccionada
opcion_seleccionada = tk.IntVar(value=0)

# Crear objetos Radiobutton con valores asociados y texto
opcion1 = tk.Radiobutton(root, text="Opción 1", variable=opcion_seleccionada, value=1)
opcion2 = tk.Radiobutton(root, text="Opción 2", variable=opcion_seleccionada, value=2)
opcion3 = tk.Radiobutton(root, text="Opción 3", variable=opcion_seleccionada, value=3)
opcion4 = tk.Radiobutton(root, text="Opción 4", variable=opcion_seleccionada, value=4)

# Crear función para reiniciar la selección de opciones
def reiniciar():
    opcion_seleccionada.set(0)

# Crear etiqueta para mostrar la opción seleccionada actualmente
etiqueta_opcion = tk.Label(root, text="Ninguna opción seleccionada")

# Empaquetar objetos Radiobutton y botón de reinicio en un contenedor Frame
contenedor_opciones = tk.Frame(root)
opcion1.pack(side="top", anchor="w")
opcion2.pack(side="top", anchor="w")
opcion3.pack(side="top", anchor="w")
opcion4.pack(side="top", anchor="w")
tk.Button(contenedor_opciones, text="Reiniciar", command=reiniciar).pack(side="bottom", pady=10)

# Empaquetar contenedor Frame y etiqueta en la ventana principal
contenedor_opciones.pack(side="left", padx=20)
etiqueta_opcion.pack(side="right", padx=20, pady=20)

# Crear función que se ejecutará cuando se seleccione una opción
def opcion_seleccionada_cambiada():
    opcion = opcion_seleccionada.get()
    if opcion == 1:
        etiqueta_opcion.config(text="Opción 1 seleccionada")
    elif opcion == 2:
        etiqueta_opcion.config(text="Opción 2 seleccionada")
    elif opcion == 3:
        etiqueta_opcion.config(text="Opción 3 seleccionada")
    elif opcion == 4:
        etiqueta_opcion.config(text="Opción 4 seleccionada")
    else:
        etiqueta_opcion.config(text="Ninguna opción seleccionada")

# Asociar la función opcion_seleccionada_cambiada a la variable IntVar
opcion_seleccionada.trace("w", lambda name, index, mode, sv=opcion_seleccionada: opcion_seleccionada_cambiada())

root.mainloop()
