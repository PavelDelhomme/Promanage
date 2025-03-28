from django.contrib import admin
from .models import CurriculumVitae, CVEntry

@admin.register(CurriculumVitae)
class CurriculumVitaeAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_public', 'created_at')
    list_filter = ('is_public', 'created_at')
    search_fields = ('title', 'user__username')

@admin.register(CVEntry)
class CVEntryAdmin(admin.ModelAdmin):
    list_display = ('cv', 'entry_type', 'title', 'start_date', 'end_date', 'order')
    list_filter = ('entry_type', 'cv')
    search_fields = ('title', 'description')
