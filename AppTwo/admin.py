from django.contrib import admin
from .models import AccessRecord,Topic,Webpage

# Register your models here.

@admin.register(AccessRecord)
class AccessRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date')

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'top_name')

@admin.register(Webpage)
class WebpageAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic', 'name', 'url')

# This version uses the __str__ function in models instead 
# admin.site.register(AccessRecord)
# admin.site.register(Topic)
# admin.site.register(Webpage)




