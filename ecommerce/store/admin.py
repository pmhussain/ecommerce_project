from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # list_display = []
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # list_display = []
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
# admin.site.register(Category)
# admin.site.register(Product)