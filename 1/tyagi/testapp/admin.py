from django.contrib import admin
from .models import post
# Register your models here.

@admin.register(post)
class posteditem(admin.ModelAdmin):
    list_display = ['id','user','text','created_at','updated_at']
