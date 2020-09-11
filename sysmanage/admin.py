from django.contrib import admin
from .models import Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent', 'level')


admin.site.register(Menu, MenuAdmin)
