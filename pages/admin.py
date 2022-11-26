from django.contrib import admin
from .models import  University,Admission,Contact
from import_export.admin import ImportExportModelAdmin

# Register your models here.



admin.site.register(Admission)
admin.site.register(Contact)
@admin.register(University)
class userdata(ImportExportModelAdmin):
    pass
