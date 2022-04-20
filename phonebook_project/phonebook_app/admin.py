from django.contrib import admin

from .models import Account, Person

admin.site.register(Person)
admin.site.register(Account)
