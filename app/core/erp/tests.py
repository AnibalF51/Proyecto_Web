from config.asgi import *
from core.erp.models import Type

#Listar

# select * from Tabla
# query = Type.objects.all()
# print(query)

#insercion
# t = Type(name='Alksjdkjs23').save()

# t = Type()
# t.name = 'Purekjas'
# t.save()

#edicion
try:
    t = Type.objects.get(pk=1)
    t.name = 'Presidente'
    t.save()
except Exception as e:
    print(e)

#eliminacion
# t = Type.objects.get(pk = 1)
# t.delete()