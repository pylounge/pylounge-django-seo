from django.contrib import admin
from .models import Exhibit
# Register your models here.
class ExhibitAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'slug')
    prepopulated_fields = {'slug': ('title', )}
    
admin.site.register(Exhibit, ExhibitAdmin)