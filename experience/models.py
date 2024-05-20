from django.db import models

class Experience(models.Model):
    title = models.CharField(max_length=50)
    companyname = models.CharField(max_length=50, blank=True)
    startdate = models.DateField(blank=True)
    enddate = models.DateField(blank=True, null = True)
    worklocation = models.CharField(max_length=50,blank=True)
    companydescription = models.CharField(max_length=550, blank=True)
    jobdescription = models.CharField(max_length=5550,blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
