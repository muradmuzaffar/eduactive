from django.contrib import admin
from .models import  University
from import_export.admin import ImportExportModelAdmin

# Register your models here.




@admin.register(University)
class userdata(ImportExportModelAdmin):
    pass
