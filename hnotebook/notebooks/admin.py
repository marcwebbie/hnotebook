from django.contrib import admin

from .models import Notebook, Housing, Review, Note

class NotebookAdmin(admin.ModelAdmin):
    model = Notebook

class HousingAdmin(admin.ModelAdmin):
    model = Housing

class ReviewAdmin(admin.ModelAdmin):
    model = Review

class NoteAdmin(admin.ModelAdmin):
    model = Note


admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Housing, HousingAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Note, NoteAdmin)
