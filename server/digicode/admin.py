from django.contrib import admin
import models

admin.site.register(models.Local)

class CodeAdmin(admin.ModelAdmin):
    list_display = ('proprietaire', 'touches') #, 'locaux')
admin.site.register(models.Code, CodeAdmin)


class AccesAdmin(admin.ModelAdmin):
    list_display = ('local', 'user', 'responsable')
admin.site.register(models.Acces, AccesAdmin)

