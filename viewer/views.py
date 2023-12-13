from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, FormView
from viewer.models import *
from django.forms import Form, ModelChoiceField, Textarea, IntegerField, CharField, ModelMultipleChoiceField, CheckboxSelectMultiple, ModelForm, DateField, SelectDateWidget, DateInput


# Create your views here.


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
    countries = ModelChoiceField(queryset=Country.objects)
    genres = ModelChoiceField(queryset=Genre.objects)
    directors = ModelChoiceField(queryset=Person.objects)
    actors = ModelChoiceField(queryset=Person.objects)
    year = IntegerField(min_value=1900, max_value=2030) #TODO: Pozor pri max_value o par rokov to nebude platit, cize to nejako vyriesit
    video = CharField(max_length=128)
    description = CharField(widget=Textarea, required=False)
    
class MovieCreateView(FormView):
    template_name = "movie_create.html"
    form_class = MovieForm


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

# Pomocou ListView
class PersonsListView(ListView):
    template_name = "persons2.html"
    model = Person
    
#TODO: vytvorit CBV, ktora zvlast zobrazi actors a directors, lepsia templateview

def person(request, pk):
    person_obj = Person.objects.get(id=pk)
    context = {"person": person_obj}
    return render(request, "person.html", context)

