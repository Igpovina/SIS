from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Profile)
admin.site.register(models.Course)
admin.site.register(models.Classes)
admin.site.register(models.Student)