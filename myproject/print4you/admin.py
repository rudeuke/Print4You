from django.contrib import admin

from .models import *

admin.site.register(Address)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Printout)
