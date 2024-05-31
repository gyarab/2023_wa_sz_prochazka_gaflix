from django.shortcuts import render

from .models import Movie, Director, Actor, Genre


def movies(request):
    context = {"movies": Movie.objects.all().order_by('name')}
    return render(request, "filmy/movies.html", context)