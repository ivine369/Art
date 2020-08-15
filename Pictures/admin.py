from django.contrib import admin
from .models import Category,Picture

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
admin.site.register(Category,CategoryAdmin)


class PictureAdmin(admin.ModelAdmin):
    list_display = ['name', 'id','category', 'location', 'created', 'updated']
    admin.site= ['created', 'updated','category']
    list_editable = ['location','category']
