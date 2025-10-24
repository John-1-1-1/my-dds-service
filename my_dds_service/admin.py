from django.contrib import admin
from .models import (
    TransactionStatus,
    TransactionType,
    Category,
    Subcategory
)


admin.site.register(TransactionStatus)
admin.site.register(TransactionType)
admin.site.register(Category)
admin.site.register(Subcategory)