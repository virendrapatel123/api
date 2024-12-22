from django.contrib import admin
from .models import Product,Showroom
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('id','name','price','description','created_at')

@admin.register(Showroom)
class ShowroomAdmin(admin.ModelAdmin):
    list_display=('name','location')