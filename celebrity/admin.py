from celebrity.models import Celebrity
from django.contrib import admin

class CelebAdmin(admin.ModelAdmin):
    list_display = ('name', 'flagged', 'whitelisted')
    search_fields = ('name', 'flagged', 'whitelisted') 
    list_editable = ('whitelisted',)
    list_filter = ('flagged',)

admin.site.register(Celebrity, CelebAdmin)
