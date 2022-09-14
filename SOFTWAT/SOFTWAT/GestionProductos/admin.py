from django.contrib import admin

from django.contrib import admin

from . models import category,Product, marca

admin.site.register(category) #se registra categoria 
#admin.site.register(Product) # se registra producto
admin.site.register(marca) # se registra marca

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'marca']
    list_display_links = ['price', 'marca']
    #list_editable = ['price']
    search_fields = ['name']
    list_filter = ['category']
    list_per_page = 2 