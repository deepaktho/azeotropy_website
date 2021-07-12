from django.contrib import admin
from .models import Extendeduser
from import_export.admin import ImportExportModelAdmin
# Register your models here.
 
@admin.register(Extendeduser)
class userdetails(ImportExportModelAdmin):
    pass