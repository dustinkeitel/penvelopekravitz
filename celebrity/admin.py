from celebrity.models import Celebrity
from django.contrib import admin

class CelebAdmin(admin.ModelAdmin):
    list_display = ('name', 'add_date', 'contributor')
    search_fields = ('name', ) 

admin.site.register(Celebrity, CelebAdmin)
