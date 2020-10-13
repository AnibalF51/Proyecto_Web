from django.db.transaction import rollback

from config.wsgi import *
from core.erp.models import *

# INSERTAR
# try:
#     t = Category(name='Lacteos').save()
# except Exception as e:
#     print(e)

# LISTAR

print(Category.objects.all())

for i in Category.objects.filter():
    print(i)