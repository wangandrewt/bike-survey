from django.conf.urls import patterns, url

from bikesurvey import views

urlpatterns = patterns('',
    # ex: /survey/
    url(r'^$', views.index, name='index'),
    # ex: /survey/5/
    url(r'^(?P<surveyInstance_id>\d+)/$', views.detail, name='detail'),
    # ex: /survey/5/record/
    url(r'^(?P<surveyInstance_id>\d+)/record/$', views.record, name='record'),
)
