from django.contrib import admin
from testapp.models import Info
# Register your models here.
class Info_Admin(admin.ModelAdmin):
    list_display=['name','mobile_no']
admin.site.register(Info,Info_Admin)
