lista_input=input("Dame una lista de países separados por comas: ")
lista_input=list(set(lista_input.split(",")))
lista_input.sort()
print("Lista de países: ", ", ".join(lista_input))
    