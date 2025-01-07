from django.contrib import admin

# Register your models here.
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","email","date_of_birth","grade","address")
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('grade', 'date_of_birth')