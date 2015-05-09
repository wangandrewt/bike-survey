from django.contrib import admin
from bikesurvey.models import SurveyInstance, Biker


class BikerInline(admin.TabularInline):
    model = Biker
    extra = 0


class SurveyInstanceAdmin(admin.ModelAdmin):
    inlines = [BikerInline]
    list_filter = ['location']

admin.site.register(SurveyInstance, SurveyInstanceAdmin)
