from django.contrib import admin
from .models import *


class AdminDoor(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category,CategoryAdmin)
admin.site.register(Door,AdminDoor)
