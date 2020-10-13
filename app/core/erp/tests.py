from config.asgi import *
from core.erp.models import Type, Employee

#Listar

# select * from Tabla
# query = Type.objects.all()
# print(query)

#insercion
# t = Type(name='hola').save()

# t = Type()
# t.name = 'Purekjas'
# t.save()

#edicion
# try:
#     t = Type.objects.get(pk=1)
#     t.name = 'Presidente'
#     t.save()
# except Exception as e:
#     print(e)

#eliminacion
# t = Type.objects.get(pk = 1)
# t.delete()

# obj = Type.objects.filter(name__contains='pre')
# obj = Type.objects.filter(name__icontains='terry')
# obj = Type.objects.filter(name__startswith='p')
# obj = Type.objects.filter(name__endswith='a')
# obj = Type.objects.filter(name__exact='prueba')
# obj = Type.objects.filter(name__in=['viba', 'hola']).count()
# obj = Type.objects.filter(name__icontains='a').exclude(id=5)
obj = Employee.objects.filter()

for i in Type.objects.filter(name__endswith='a'):
    print(i.name)