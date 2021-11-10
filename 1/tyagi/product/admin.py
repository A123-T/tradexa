from django.contrib import admin
from .models import producti
# Register your models here.

@admin.register(producti)
class productitem(admin.ModelAdmin):
    list_display = ['id','name','weight','price','created_at','updated_at']
