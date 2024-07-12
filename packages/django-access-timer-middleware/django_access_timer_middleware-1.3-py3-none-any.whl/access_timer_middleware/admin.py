from django.contrib import admin

# Register your models here.

from access_timer_middleware import models


@admin.register(models.AccessTime)
class Admin(admin.ModelAdmin):
    pass
