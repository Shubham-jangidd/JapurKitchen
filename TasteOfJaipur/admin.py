from django.contrib import admin

# Register your models here.

from .models import contactus

@admin.register(contactus)
class contactusModelAdmin(admin.ModelAdmin):
    """Show models in admin panel."""

    list_display = ["first_name", "email", "message"]
