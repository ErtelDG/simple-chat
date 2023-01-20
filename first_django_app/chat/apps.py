# The default_auto_field attribute is set to 'django.db.models.BigAutoField'
from django.apps import AppConfig


# The default_auto_field attribute is set to the BigAutoField class
class ChatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chat'
