from django.contrib import admin
from App.models import Registro_email

class Registro_emailAdmin(admin.ModelAdmin):
    list_display = ["email"]
    list_per_page = 10


admin.site.register(Registro_email, Registro_emailAdmin)