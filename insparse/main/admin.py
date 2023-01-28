from django.contrib import admin

# Register your models here.
from .models import (
    InspectionSource,
    InspectionLoadHistory,
    Company,
    Region,
    InspectionType,
    InspectionStatus,
    Inspection
)

admin.site.register(InspectionSource)
admin.site.register(InspectionLoadHistory)
admin.site.register(Company)
admin.site.register(Region)
admin.site.register(InspectionType)
admin.site.register(InspectionStatus)

class InspectionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Inspection._meta.get_fields()]
    list_filter = ('status__status_name', 'source__department_name',)
    search_fields = ('company__company_name', )

admin.site.register(Inspection, InspectionAdmin)