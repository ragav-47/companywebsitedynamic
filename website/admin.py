from django.contrib import admin
from .models import people,peopleAdmin
from .models import products,productsAdmin


# Register your models here.

admin.site.register(people,peopleAdmin)

admin.site.register(products,productsAdmin)