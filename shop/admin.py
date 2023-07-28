from django.contrib import admin
from .models import Product,Contact,Orders
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    
    list_display=('product_name','qty','total')
    list_filter=['category','pub_date']
    search_fields=['category']


class CustomeOrder(admin.ModelAdmin):
	list_filter=['pub_date']
	search_fields=['pub_date']


admin.site.register(Product,ProductAdmin)
admin.site.register(Contact)
admin.site.register(Orders,CustomeOrder)