from django.contrib import admin
from .models import Menu, MasterChef, SocialChef, Query, BookATable
# Register your models here.


class MenuAdmin(admin.ModelAdmin):
    list_filter = ["price",]


admin.site.register(Menu, MenuAdmin)
admin.site.register(MasterChef)
admin.site.register(SocialChef)
admin.site.register(Query)
admin.site.register(BookATable)
