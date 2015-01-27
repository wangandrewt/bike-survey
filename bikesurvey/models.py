from django.db import models

class SurveyInstance(models.Model):
    LOCATION_CHOICES=(
        ('Regents Drive @ Rt. 1', 'Regents Drive @ Rt. 1'),
        ('Mowatt Lane Garage Exit @ Knox Rd.', 'Mowatt Lane Garage Exit @ Knox Rd.'),
        ('Mall @ Woods Hall', 'Mall @ Woods Hall'),
        ('Regents Dr. @ Main Administration', 'Regents Dr. @ Main Administration'),
        ('Campus Dr. @ Paint Branch Dr.', 'Campus Dr. @ Paint Branch Dr.'),
        ('Campus Dr. @ The Stamp', 'Campus Dr. @ The Stamp'),
        ('Regents Drive @ Stadium Drive', 'Regents Drive @ Stadium Drive'),
        ('Paint Branch Drive @ Lot 11b', 'Paint Branch Drive @ Lot 11b'),
        ('Campus Drive @ Adelphi Road', 'Campus Drive @ Adelphi Road'),
    )
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200, choices=LOCATION_CHOICES)
    comments = models.TextField(blank=True)
    def __unicode__(self):
        return self.name + " at " + self.location


class Biker(models.Model):
    GENDER_CHOICES=(
        ('M', 'Male'),
        ('F', 'Female'),
    )
    HELMET_CHOICES=(
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    LOCATION_CHOICES=(
        ('Sidewalk', 'Sidewalk'),
        ('Street', 'Street'),
    )
    surveyInstance = models.ForeignKey(SurveyInstance)
    bikerGender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=None)
    bikerHelmet = models.CharField(max_length=1, choices=HELMET_CHOICES, default=None)
    bikerLocation = models.CharField(max_length=30, choices=LOCATION_CHOICES, default=None)
    time = models.TimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    def __unicode__(self):
        return "Gender: "+self.bikerGender+", Helmet: "+self.bikerHelmet+", Location: "+self.bikerLocation+" at "+self.date.strftime('%Y-%m-%d')+" at "+self.time.strftime('%H:%M')
