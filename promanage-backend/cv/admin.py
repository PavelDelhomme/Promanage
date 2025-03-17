from django.contrib import admin
from .models import CVEntry

@admin.register(CVEntry)
class CVEntryAdmin(admin.ModelAdmin):
    list_display = ('entry_type', 'title', 'start_date', 'end_date', 'is_public')
    list_filter = ('entry_type', 'is_public')
    search_fields = ('title', 'description')
