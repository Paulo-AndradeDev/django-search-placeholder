# django-search-placeholder
Auto add placeholder content for django admin

## Install
- By git
```bash
pip install git+https://hub.fastgit.org/waketzheng/django-search-placeholder.git
```

## Usage

1. Add app name to settings
```py
INSTALLED_APPS = [
    ...
    "django.contrib.admin",
    ...
    "search_placeholder",
    ...
]
```
2. Use search_placeholder.ModelAdmin to replace admin.ModelAdmin
```
from django.contrib import admin
from search_placeholder import ModelAdmin

@admin.register(ModelClass)
class ModelClassAdmin(ModelAdmin):
    # Just inherit from search_placeholder.ModelAdmin
    # it will auto generate placeholder of search input by
    # the verbose_name of 'field1' and 'field2'
    # Or you can uncomment the next line to custom placeholder
    #search_placeholder = 'Custom content'
    search_fields = ('field1', 'field2')
```
