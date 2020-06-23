from django.contrib import admin

from .models import uploadFiles

class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'fileL', 'fname', 'up_date']
admin.site.register(uploadFiles, BookAdmin)
