from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=300)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    footage = models.PositiveSmallIntegerField(blank=True, null=True, help_text="in minutes")
    description = models.TextField(blank=True)
    director = models.ForeignKey('Director',blank= True, null= True, on_delete= models.SET_NULL) # 'Director' must be in '' cause it is defined later
    main_picture = models.CharField(blank=True, default="", max_length=2048)
    actors = models.ManyToManyField('Actor', blank= True)
    genres = models.ManyToManyField('Genre', blank= True)
    def __str__(self):
        return self.name
    # help function that gets all geners and seperates them by ,
    def genres_display(self):
        return ",".join(i.name for i in self.genres.all()) # rozdělí string čárkou
class Director(models.Model):
    name = models.CharField(max_length=300)
    birth_year = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    main_picture = models.CharField(blank=True, default="", max_length=2048)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=300)
    birth_year = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    main_picture = models.CharField(blank=True, default="", max_length=2048)

    def __str__(self):
        return self.name    