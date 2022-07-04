from django.contrib import admin
from .models import Poll

# Register your models here.

class PollAdmin(admin.ModelAdmin):
    list_display = ('question',)
    search_fields = ('question',)

admin.site.register(Poll)