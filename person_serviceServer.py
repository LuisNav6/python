from spyne import Application, rpc, ServiceBase, Unicode, Integer, ComplexModel, Array
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class Person(ComplexModel):
    name = Unicode
    age = Integer
    id = Integer
    phone = Unicode
    email = Unicode
    
class PersonService(ServiceBase):
    persons = {}  # Mueve la variable persons fuera del constructor

    @rpc(Unicode, Integer, Integer,Unicode,Unicode, _returns=Integer)
    def addPerson(ctx, name, age, _id, phone, email):
        person = Person(name=name, age=age, id=_id, phone = phone, email = email )
        PersonService.persons[_id] = person
        return 1  # Return some indicator of success

    @rpc(Integer, _returns=Integer)
    def deletePerson(ctx, _id):
        if _id in PersonService.persons:
            del PersonService.persons[_id]
            return 1  # Person deleted successfully
        return 0  # Person not found

    @rpc(Integer, _returns=Person)
    def getPerson(ctx, _id):
        return PersonService.persons.get(_id)
    

    @rpc(_returns=Array(Person))
    def getAllPersons(ctx):
        return list(PersonService.persons.values())

application = Application([PersonService], 'http://example.com/persons', in_protocol=Soap11(validator='lxml'), out_protocol=Soap11())
wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    import logging
    from wsgiref.simple_server import make_server

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    server = make_server('localhost', 8000, wsgi_application)
    server.serve_forever()
