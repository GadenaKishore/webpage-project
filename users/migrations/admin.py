from django.contrib import admin
from users.models import registrationmodel

# Register your models here.
class registredtable(admin.ModelAdmin):
    list_display = ('name','username','mobile','email')
admin.site.register(registrationmodel,registredtable)
