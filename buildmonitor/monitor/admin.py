from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import BuildJob

@admin.register(BuildJob)
class BuildJobAdmin(admin.ModelAdmin):
    list_display  = ('name', 'status', 'branch', 'triggered_by', 'created_at')
    list_filter   = ('status', 'branch')
    search_fields = ('name',)