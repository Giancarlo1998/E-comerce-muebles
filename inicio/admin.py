from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ('nombre', 'price','linkjc', 'view_count','dimensiones',)
	list_editable = ('price','linkjc', 'view_count','dimensiones',)
	search_fields = ('nombre', 'linkjc',)
	#list_filter = ('business',)
	#exclude = ('name',	)

@admin.register(Category)
class CatAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ('nombre',)
	#list_editable = ('available',)
	#search_fields = ('id',)
	#list_filter = ('nombre',)
	#exclude = ('name',	)


@admin.register(ProductImage)
class ProductImageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ('product',)
	

