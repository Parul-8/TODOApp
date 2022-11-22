from django.contrib import admin
from app.models import TODO

# Register your models here.
#registering our todo model with admin module
admin.site.register(TODO)
