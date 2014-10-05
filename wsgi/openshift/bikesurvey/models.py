from django.db import models


class SurveyInstance(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date = models.DateField()
    def __unicode__(self):
        return self.name + " at " + self.location + " at " + self.date.strftime('%Y-%m-%d')


class Biker(models.Model):
    surveyInstance = models.ForeignKey(SurveyInstance)
    bikerGender = models.CharField(max_length=50)
    bikerHelmet = models.CharField(max_length=50)
    bikerLocation = models.CharField(max_length=50)
    count = models.IntegerField(default=0)
    def __unicode__(self):
        return "Gender: "+self.bikerGender+", Helmet: "+self.bikerHelmet+", Location: "+self.bikerLocation
