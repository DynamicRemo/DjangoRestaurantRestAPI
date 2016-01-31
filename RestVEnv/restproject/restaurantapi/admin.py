from django.contrib import admin
from restaurantapi.models import Menu, MenuItem

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    # pass
    list_display = ['id', 'name', 'description', 'chef', 'available']

class MenuItemAdmin(admin.ModelAdmin):
    # pass
    list_display = ['id', 'name', 'description', 'cost_to_make', 'sale_price', 'available', 'menu']

admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)