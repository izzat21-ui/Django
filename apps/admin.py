from django.contrib import admin

from apps.models import Job


# Register your models here.
@admin.register(Job)
class ProductAdmin(admin.ModelAdmin):
    pass
