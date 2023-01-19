from django.contrib import admin
from .models import Message
class MessageAdmin(admin.ModelAdmin):
 fields = ('text', 'created_At', 'author', 'receiver')
 list_display = ( 'created_At', 'author', 'text', 'receiver')
 search_fields = ('text',)

# Register your models here.
admin.site.register(Message, MessageAdmin)