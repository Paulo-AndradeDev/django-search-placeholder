from django.contrib import admin

from .mixins import PlaceholderMixin


class ModelAdmin(PlaceholderMixin, admin.ModelAdmin):
    ...
