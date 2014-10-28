from django.contrib import admin

from .models import Notebook

class NotebookAdmin(admin.ModelAdmin):
    model = Notebook

admin.site.register(Notebook, NotebookAdmin)
