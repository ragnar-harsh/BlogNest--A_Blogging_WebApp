from django.contrib import admin
from contactModel.models import contactModel

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')

admin.site.register(contactModel, ContactAdmin)

# Register your models here.
