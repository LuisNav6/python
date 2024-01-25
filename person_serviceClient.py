# person_serviceClient.py

from zeep import Client

# Crear un cliente para el servicio SOAP
client = Client('http://localhost:8000/persons?wsdl')

# Agregar una persona
response_add = client.service.addPerson(name='Humberto', age=30, _id=3, phone = "4491234568", email ="luis@gmail.com")  # Cambiar 'id' a '_id'
print("Add Person Status:", response_add)

# Obtener todas las personas
response_get_all = client.service.getAllPersons()
print("All Persons:", response_get_all)

# Obtener una persona por ID
#response_get = client.service.getPerson(_id=1)  # Cambiar 'id' a '_id'
#print("Get Person:", response_get)

# Eliminar una persona por ID
#response_delete = client.service.deletePerson(_id=1)  # Cambiar 'id' a '_id'
#print("Delete Person Status:", response_delete)
