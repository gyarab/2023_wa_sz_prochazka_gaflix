from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length = 300)
    year = models.PositiveSmallIntegerField(blank = True, null = True)
    footage = models.PositiveSmallIntegerField(blank = True,null = True,
                                               help_text= "in minutes")
    