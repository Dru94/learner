from ast import Sub
from django.contrib import admin
from .models import Notes, Subjects

# Register your models here.
admin.site.register(Notes)
admin.site.register(Subjects)