"""
URL configuration for hollymovie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from viewer.models import Genre, Movie, Country, Person, Rating, Comment, Image
from viewer.views import *

admin.site.register(Country)
admin.site.register(Genre)
admin.site.register(Person)
admin.site.register(Movie)
#admin.site.register(Rating)
admin.site.register(Comment)
admin.site.register(Image)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("hello", hello),
    path("hello2/<s>", hello2),
    path("hello3/", hello3),
    path("hello4/", hello4),
    path("hello5/<s0>", hello5),
    
    path("", index, name="index"),
    
    #path("movies/", movies, name="movies"),
    #path("movies/", MoviesView.as_view(), name="movies"),
    #path("movies/", MoviesTemplateView.as_view(), name="movies"),
    path("movies/", MoviesListView.as_view(), name="movies"),
    
    path("movie/create/", MovieFormView.as_view(), name="movie_create"),
    path("movie/<pk>/", movie, name="movie"),
    
    #path("persons/", persons, name="persons"),
    path("persons/", PersonsListView.as_view(), name="persons"),
    
    #path("person/create/", PersonFormView.as_view(), name="person_create"),
    path("person/create/", PersonCreateView.as_view(), name="person_create"),
    path("person/update/<pk>/", PersonUpdateView.as_view(), name="person_update"),

    path("person/<pk>/", person, name="person"),
    path("genre/<pk>/", movies_by_genre, name="genre"),
    path("country/<pk>/", movies_by_country, name="country"),
    
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
