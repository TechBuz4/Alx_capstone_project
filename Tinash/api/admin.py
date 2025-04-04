from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User, Category, Product, Cart, Order, OrderProduct
@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    model = User
    list_display = ("username", "email", "role", "is_seller", "is_buyer")
    list_filter = ("role",)
    search_fields = ("username", "email")
    ordering = ("username",)

    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (_("Role info"), {"fields": ("role",)}),  # ← fixed here
        (_("Permissions"), {
            "fields": ("is_buyer", "is_seller"),
        }),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "role"),
        }),
    )

# Register other models
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderProduct)
