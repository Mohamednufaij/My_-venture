from django.contrib import admin

# Register your models here.

from orders.models import Order,Ordered_item
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_filter=[
        "owner",
        "order_status",
        
    ]
    search_fields=(
        "owner",
        "id"
    )

admin.site.register(Order,OrderAdmin)