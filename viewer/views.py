from collections.abc import Mapping
from logging import getLogger
from typing import Any
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, FormView, CreateView, UpdateView, DeleteView
from viewer.models import *
from django.forms import Form, ModelChoiceField, Textarea, IntegerField, CharField, ModelMultipleChoiceField, CheckboxSelectMultiple, ModelForm, DateField, SelectDateWidget, DateInput
from datetime import datetime

# Create your views here.

LOGGER = getLogger()

def hello(request):
    return HttpResponse("Hello world!")


def hello2(request, s):
    return HttpResponse(f"Hello {s} world!")


def hello3(request):
    s = request.GET.get("s", "")
    return HttpResponse(f"Hello {s} world!")


def hello4(request):
    return render(request, template_name="hello.html")


def hello5(request, s0):
    s1 = request.GET.get('s1', '')
    context = {'adjectives': [s0, s1, 'beautiful', 'wonderful']}
    return render(
        request,
        template_name='hello5.html',
        context=context
    )


def index(request):
    return render(request, "index.html")

# Pomocou funkcie:
"""
    def movies(request):
    g = request.GET.get("genre", "")
    genres = Genre.objects.all()
    if g != "" and c != "":
        g = int(g)
        c = int(c)
        if Genre.objects.filter(id=g).exists() and Country.objects.filter(id=c).exists():
            genre = Genre.objects.get(id=g)
            country = Country.objects.get(id=c)
            movie_list = Movie.objects.filter(genres = genre, countries = country)
            context = {"movies": genre.movies_of_genre.all(), "genres": genres, "filtered_by": f"podla zanru{genre} a zeme {movies_by_country}"}
            return render(request, "movies.html", context)
    if g != "":
        g = int(g)
        if Genre.objects.filter(id=g).exists():          
            genre = Genre.objects.get(id=g)
            context = {"movies": genre.movies_of_genre.all(), "genres": genres, "filtered_by": f"podla zanru{genre}"}
            return render(request, "movies.html", context)
        else:
            context = {"movies": [], "genres": genres, "filtered_by": ""}
            return render(request, "movies.html", context)
    c = request.GET.get("country", "")
    countries = Country.objects.all()
    if c != "":
        c = int(c)
        if Country.objects.filter(id=c).exists():
            country = Country.objects.get(id=c)
            context = {"movies": country.movies_in_country.all(), "genres": genres, "filtered_by": f"podla zeme{country}"}
            return render(request, "movies.html", context)
        else:
            context = {"movies": [], "genres": genres, "filtered_by": ""}
            return render(request, "movies.html", context)
    movies_list = Movie.objects.all()
    genres_list = Genre.objects.all()
    context = {"movies": movies_list, "genres": genres_list, "filtered_by": ""}
    return render(request, "movies.html", context) 
"""
# Pomocou vseobecnej triedy View
class MoviesView(View):
    def get(self, request):
        movies_list = Movie.objects.all()
        context = {"movies": movies_list}
        return render(request, "movies.html", context)
    
# Pomocou TemplateView:
class MoviesTemplateView(TemplateView):
    template_name = "movies.html"
    extra_context = {"movies": Movie.objects.all()}

# Pomocou ListView
class MoviesListView(ListView):
    template_name = "movies2.html"
    model = Movie


def movie(request, pk):
    movie_obj = Movie.objects.get(id=pk)
    context = {"movie": movie_obj}
    return render(request, "movie.html", context)


class MovieForm(Form):
    title_orig = CharField(max_length=128)
    title_cz = CharField(max_length=128, required=False)
    title_sk = CharField(max_length=128, required=False)
    countries = ModelMultipleChoiceField(queryset=Country.objects)
    genres = ModelMultipleChoiceField(queryset=Genre.objects, widget=CheckboxSelectMultiple)
    directors = ModelMultipleChoiceField(queryset=Person.objects)
    actors = ModelMultipleChoiceField(queryset=Person.objects)
    year = IntegerField(min_value=1900, max_value=datetime.now().year + 3)
    video = CharField(max_length=128)
    description = CharField(widget=Textarea, required=False)
    
    def clean_title_orig(self):
        initial_form = super().clean()
        initial = initial_form["title_orig"].strip()
        return initial.capitalized()
    
    def clean(self):
        return super().clean()


class MovieFormView(FormView):
    template_name = "movie_create.html"
    form_class = MovieForm
    succes_url = reverse_lazy("movie_create")
    
    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        new_movie = Movie.objects.create(
            title_orig = cleaned_data["title_orig"],
            title_cz = cleaned_data["title_cz"],
            title_sk = cleaned_data["title_sk"],
            #countries = cleaned_data["countries"],
            #genres = cleaned_data["genres"],
            #directors = cleaned_data["directors"],
            #actors = cleaned_data["actors"],
            year = cleaned_data["year"],
            video = cleaned_data["video"],
            description = cleaned_data["description"],
        )
        new_movie.countries.set(cleaned_data["countries"])
        new_movie.genres.set(cleaned_data["genres"])
        new_movie.directors.set(cleaned_data["directors"])
        new_movie.actors.set(cleaned_data["actors"])
        new_movie.save()
        return result
    
    def form_invalid(self, form):
        LOGGER.warning("User provided invalid data.")
        return super().form_invalid(form)

def movies_by_genre(request, pk):
    genre_movies = Genre.objects.get(id=pk)
    genres_list = Genre.objects.all()
    context = {"movies": genre_movies.movies_of_genre.all(), "genres": genres_list}
    return render(request, "movies.html", context )

def movies_by_country(request, pk):
    country_movies = Country.objects.get(id=pk)
    countries_list = Country.objects.all()
    context = {"movies": country_movies.movies_in_country.all(), "countries": countries_list}
    return render(request, "movies.html", context)


def persons(request):
    persons_list = Person.objects.all()
    actors_list = Person.objects.filter(acting_movie__isnull=False).distinct()
    directors_list = Person.objects.filter(directing_movie__isnull=False).distinct()
    context = {"persons": persons_list, "actors": actors_list, "directors": directors_list}
    return render(request, "persons.html", context)


class PersonModelForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["birth_date"].widget = DateInput(
            attrs={
                "type": "date",
                "placeholder": "dd-mm-yyyy",
                "class": "form-control"
            }
        )
    
    class Meta:
        model = Person
        fields = "__all__"  #- zobrazuje sa vsetko
        # fields = ["first_name", "Last_name"] # da sa menit aj poradie len prehodenim ...
        # exclude = ["biography"] - zoznam vsetkeho okrem toho co je v zozname

    def clean_first_name(self):
        initial_form = super().clean()
        initial = initial_form["first_name"].strip()
        return initial.capitalized()
    
    def clean_last_name(self):
        initial_form = super().clean()
        initial = initial_form["last_name"].strip()
        return initial.capitalized()
    
    def clean(self):
        return super().clean()
        
class PersonFormView(FormView):
    template_name = "person_create.html"
    form_class = PersonModelForm
    succes_url = reverse_lazy("person_create")
    
    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Person.objects.create(
            first_name = cleaned_data["first_name"],
            last_name = cleaned_data["last_name"],
            birth_date = cleaned_data["birth_date"],
            death_date = cleaned_data["death_date"],
            age = cleaned_data["age"],
            biography = cleaned_data["biography"],
        )
        return result
    
    def form_invalid(self, form):
        LOGGER.warning("User provided invalid data.")
        return super().form_invalid(form)

class PersonCreateView(CreateView):
    template_name = "person_create.html"
    form_class = PersonModelForm
    succes_url = reverse_lazy("person_create")
    
    def form_invalid(self, form):
        LOGGER.warning("User provided invalid data.")
        return super().form_invalid(form)
    
class PersonUpdateView(UpdateView):
    template_name = "person_create.html"
    model = Person
    form_class = PersonModelForm
    succes_url = reverse_lazy("persons")
    
    def form_invalid(self, form):
        LOGGER.warning("User provided invalid data.")
        return super().form_invalid(form)

    
"""
Rozsirenejsia verzia ako pri MovieForm (vid vyssie)

    class PersonForm(Form):
    first_name = CharField(max_length=32)
    last_name = CharField(max_length=32)
    birth_date = DateField()
    death_date = DateField()
    age = IntegerField()
    biography = TextField()
    
    def clean_first_name(self):
        initial_form = super().clean()
        initial = initial_form["first_name"].strip()
        return initial.capitalized()
    
    def clean_last_name(self):
        initial_form = super().clean()
        initial = initial_form["last_name"].strip()
        return initial.capitalized()
    
    def clean(self):
        return super().clean()

class PersonFormView(FormView):
    template_name = "person_create.html"
    form_class = PersonForm
    succes_url = reverse_lazy("person_create")
    
    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Person.objects.create(
            first_name = cleaned_data["first_name"],
            last_name = cleaned_data["last_name"],
            birth_date = cleaned_data["birth_date"],
            death_date = cleaned_data["death_date"],
            age = cleaned_data["age"],
            biography = cleaned_data["biography"],
        )
        return result
    
    def form_invalid(self, form):
        LOGGER.warning("User provided invalid data.")
        return super().form_invalid(form)
"""
# Pomocou ListView
class PersonsListView(ListView):
    template_name = "persons2.html"
    model = Person
    
#TODO: vytvorit CBV, ktora zvlast zobrazi actors a directors, lepsia templateview

def person(request, pk):
    person_obj = Person.objects.get(id=pk)
    context = {"person": person_obj}
    return render(request, "person.html", context)

