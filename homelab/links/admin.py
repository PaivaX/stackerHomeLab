from django.contrib import admin
from .models import Link

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'open_in_new_tab', 'active')
    list_filter = ('active', 'open_in_new_tab')
    search_fields = ('name', 'description', 'url')
    list_editable = ('active',)
