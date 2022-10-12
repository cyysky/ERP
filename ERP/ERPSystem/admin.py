from django.contrib import admin
from .models import Sales_Order

class imageAdmin(admin.ModelAdmin):
    list_display = ["title", "image_tag", "photo"] # new

admin.site.register(Sales_Order, imageAdmin)