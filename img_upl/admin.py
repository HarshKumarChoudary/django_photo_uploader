from django.contrib import admin
from .models import imageTable

@admin.register (imageTable)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','image','date']





# Register your models here.
