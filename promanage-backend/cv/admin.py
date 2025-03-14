from django.contrib import admin
from .models import CVEntry

@admin.register(CVEntry)
class CVEntryAdmin(admin.ModelAdmin):
    list_display = ('entry_type', 'title', 'start_date', 'is_public')
    list_filter = ('entry_type', 'is_public')