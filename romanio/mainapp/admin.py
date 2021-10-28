from django.contrib import admin
from .models import *


class AdminDoor(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class MainCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class AdminWindow(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(MainCategory,MainCategoryAdmin)
admin.site.register(Door,AdminDoor)
admin.site.register(Window,AdminWindow)
