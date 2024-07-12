from django.contrib import admin

# Register your models here.

from backend.access_timer_middleware.src.access_timer_middleware import models


@admin.register(models.AccessTime)
class Admin(admin.ModelAdmin):
    pass
