from django.contrib import admin
from .models import  University,Admission
from import_export.admin import ImportExportModelAdmin

# Register your models here.



admin.site.register(Admission)
@admin.register(University)
class userdata(ImportExportModelAdmin):
    pass
