from django.contrib import admin
from .models import todomodel

class todoAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "datecomplete")


admin.site.register(todomodel, todoAdmin)