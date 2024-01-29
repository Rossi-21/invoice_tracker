from django.contrib import admin
from .models import *


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'total', 'department', 'date', 'created_at')
    list_filter = ('vendor', 'department', 'date')
    search_fields = ['vendor__name']


admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Vendor)
admin.site.register(Department)
