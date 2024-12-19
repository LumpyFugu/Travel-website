from django.contrib import admin

# Register your models here.

from .models import Travellerinf,Comments
#@admin.register(Travellerinf)
class TravellerinfAdmin(admin.ModelAdmin):
    list_display = ['name', 'pwd', 'head']

#from .models import Comments
admin.site.register(Comments)