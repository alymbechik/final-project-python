from django.contrib import admin
from .models import Food, Category, Lead

class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'created_date')
    search_fields = ('name', 'email')
    list_filter = ('created_date', )

admin.site.register(Food)
admin.site.register(Category)
admin.site.register(Lead, LeadAdmin)