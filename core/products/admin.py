from django.contrib import admin

from . import models

admin.site.register(models.Car)
admin.site.register(models.News)
admin.site.register(models.Product)