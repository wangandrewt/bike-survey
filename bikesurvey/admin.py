from django.contrib import admin
from bikesurvey.models import SurveyInstance, Biker


class BikerInline(admin.TabularInline):
    model = Biker
    extra = 0

class SurveyInstanceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'location']}),
    ]
    inlines = [BikerInline]
    list_display = ('name', 'location')
    list_filter = ['location']
    
admin.site.register(SurveyInstance, SurveyInstanceAdmin)
