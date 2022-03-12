from django.contrib import admin

from .models import Person, Account

admin.site.register(Person)
admin.site.register(Account)
