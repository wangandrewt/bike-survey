from django.contrib import admin
from bikesurvey.models import SurveyInstance, Biker


class BikerInline(admin.TabularInline):
    model = Biker
    extra = 2

class SurveyInstanceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'date', 'location']}),
    ]
    inlines = [BikerInline]
    list_display = ('name', 'date', 'location')
    list_filter = ['date']
    
admin.site.register(SurveyInstance, SurveyInstanceAdmin)
