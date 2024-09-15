# admin.py
from django.contrib import admin
from .models import ExcelFile


@admin.register(ExcelFile)
class ExcelFileAdmin(admin.ModelAdmin):
    list_display = ['name', 'uploaded_at']