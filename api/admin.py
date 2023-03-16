from django.contrib import admin

from api.models import Company, Employee, ExternalUser


# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'type')
    search_fields = ('name',)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company')
    search_fields = ('name',)


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'address')
    search_fields = ('name',)


admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(ExternalUser, UserAdmin)
