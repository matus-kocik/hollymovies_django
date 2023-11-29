from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model, CharField, IntegerField, TextField, DateField, ForeignKey, ManyToManyField, SET_NULL, DO_NOTHING

# Create your models here.

class Country(Model):
    name = CharField(max_length=64, null=False, blank=False)
    
    class Meta:
        verbose_name_plural = "Countries"
    
    def __str__(self) -> str:
        return f"{self.name}"

class Genre(Model):
    name = CharField(max_length=128, null=False, blank=False) # CharField => VARCHAR
    
    def __str__(self) -> str:
        return f"{self.name}"
    
class Person(Model):
    first_name = CharField(max_length=32, null=False, blank=False)
    last_name = CharField(max_length=32, null=False, blank=False)
    birth_date = DateField(null=True, blank=True)
    biography = TextField(null=True, blank=True)
    
    class Meta:
        ordering = ["last_name", "first_name"]
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
class Movie(Model):
    title_orig = CharField(max_length=128, null=False, blank=False)
    title_cz = CharField(max_length=128, null=True, blank=True)
    title_sk = CharField(max_length=128, null=True, blank=True)
    countries = ManyToManyField(Country, blank=True, related_name="movies_in_country")
    genres = ManyToManyField(Genre, blank=True, related_name="movies_of_genre")
    directors = ManyToManyField(Person, blank=False, related_name="directing_movie")
    actors = ManyToManyField(Person, blank=True, related_name="acting_movie")
    year = IntegerField(null=True, blank=True)
    video = CharField(max_length=128, null=True, blank=True)
    description = TextField(null=True, blank=True)

    def __str__(self) -> str:
        # TODO: pokial existuje nazov cesky alebo slovensky tak zobrazit a ak ne tak ENG + do zatvorky rok
        # Pr: Forrest Gump (1994)
        return f"{self.title_orig}"

class Rating(Model):
    movie = ForeignKey(Movie, on_delete=DO_NOTHING, null=False, blank=False)
    user = ForeignKey(User, null=True, on_delete=SET_NULL)
    rating = IntegerField(null=False, blank=False)
    
"""     def __str__(self) -> str:
        return f"{self.name}" """
    
class Comment(Model):
    movie = ForeignKey(Movie, on_delete=DO_NOTHING)
    user = ForeignKey(User, null=True, on_delete=SET_NULL)
    comment = TextField(null=False, blank=False)
    
"""     def __str__(self) -> str:
        return f"{self.name}" """

class Image(Model):
    movie = ForeignKey(Movie, on_delete=DO_NOTHING, null=False, blank=False)
    url = CharField(max_length=128, null=False, blank=False)
    description = TextField()
    
"""     def __str__(self) -> str:
        return f"{self.name}" """