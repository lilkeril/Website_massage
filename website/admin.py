from django.contrib import admin
from .models import User, Service, Recording


@admin.register(User)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(Recording)
class RecordingAdmin(admin.ModelAdmin):
    pass

