from django.contrib import admin
from .models import Theory

class TheoryAdmin(admin.ModelAdmin):
    list_display = ('level', 'topic', 'file')
    list_filter = ('level',)
    search_fields = ('topic',)

admin.site.register(Theory, TheoryAdmin)