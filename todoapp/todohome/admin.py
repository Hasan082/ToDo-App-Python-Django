from django.contrib import admin
from .models import todomodel

class todoAdmin(admin.ModelAdmin):
    list_display = ("firstName", "lastName")


admin.site.register(todomodel, todoAdmin)