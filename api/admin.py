from django.contrib import admin
from api.models import Note

class APIAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Note, APIAdmin)
