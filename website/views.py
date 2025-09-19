from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
import os
from django.db import IntegrityError
from dotenv import load_dotenv
import requests
from django.shortcuts import render, redirect
from django.contrib import messages
load_dotenv()


def main_page(request):
    return render(request, "main_page.html")


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main_page')
        else:
            return render(request, 'login_page.html', {'error': 'Invalid username or password'})

    return render(request, 'login_page.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            login(request, user)
            return redirect('main_page')
        except IntegrityError:
            messages.error(
                request, "User exists already")
            return redirect('register')

    return render(request, 'registration_page.html')


def advised(request):
    url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": os.getenv('TMDB_API')
    }

    response = requests.get(url, headers=headers)
    movies = dict(response.json())['results']
    movies_list = [{"title": m["title"], "poster": m["poster_path"]}
                   for m in movies]
    context = {"movies": movies_list}

    return render(request, "movies_advised.html", context)


def top_picks(request):
    return render(request, 'top_picks.html')


def watched_movies(request):
    return render(request, 'watched_movies.html')


def load_more(request):
    page = request.GET.get("page", 1)
    url = f"https://api.themoviedb.org/3/movie/popular?language=en-US&page={page}"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.getenv('TMDB_API')}"
    }
    response = requests.get(url, headers=headers)
    movies = response.json().get("results", [])

    next_page = int(page) + 1
    return render(request, "movies_advised.html", {"movies": movies, "next_page": next_page})


def logout_func(request):
    logout(request)
    return redirect('main_page')
