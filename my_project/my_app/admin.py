from django.contrib import admin


from .models import *
# Register your models here.


class adminCrud(admin.ModelAdmin):
    list_display=("task","is_completes","updates_at")
    # search_fields=("task")
    


admin.site.register(Product)
admin.site.register(Item)
admin.site.register(Crud,adminCrud)
admin.site.register(Catogory)
admin.site.register(Signup)
admin.site.register(demo)
admin.site.register(Book)
admin.site.register(Youtube_thum)
admin.site.register(Books)