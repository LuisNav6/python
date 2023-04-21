import tkinter as tk

# Crear la ventana principal
root = tk.Tk()

# Crear una lista de opciones
opciones = ["Opción 1", "Opción 2", "Opción 3", "Opción 4"]

# Crear una variable de control para la selección
seleccion = tk.StringVar(value=opciones[0])

# Crear una etiqueta de texto
label = tk.Label(root, text="Selecciona una opción:")

# Crear un menú de opciones
menu = tk.OptionMenu(root, seleccion, *opciones)

# Posicionar los widgets en la ventana
label.pack()
menu.pack()

# Iniciar el bucle principal de la aplicación
root.mainloop()
