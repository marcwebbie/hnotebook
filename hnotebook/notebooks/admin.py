from django.contrib import admin

from .models import Notebook, Housing

class NotebookAdmin(admin.ModelAdmin):
    model = Notebook

class HousingAdmin(admin.ModelAdmin):
    model = Housing

admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Housing, HousingAdmin)
