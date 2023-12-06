from django.http import HttpResponse
from django.shortcuts import render
from viewer.models import *


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


def movies(request):
    movies_list = Movie.objects.all()
    genres_list = Genre.objects.all()
    countries_list = Country.objects.all()
    context = {"movies": movies_list, "genres": genres_list, "countries": countries_list}
    return render(request, "movies.html", context)


def movie(request, pk):
    movie_obj = Movie.objects.get(id=pk)
    context = {"movie": movie_obj}
    return render(request, "movie.html", context)

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
    context = {"persons": persons_list}
    return render(request, "persons.html", context)

def person(request, pk):
    person_obj = Person.objects.get(id=pk)
    context = {"person": person_obj}
    return render(request, "person.html", context)

