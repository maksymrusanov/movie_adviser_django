from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout


def main(request):
    return render(request, 'main.html')


def login(request):
    if request.method == 'POST':
        user = User.objects.get(request.POST)

        return redirect('main', user)
    return render(request, 'login_page.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(request.POST)
        return redirect('main')  # важно вернуть redirect

    return render(request, 'registration_page.html')


def advised(request):
    return render(request, 'movies_advised.html')


def top_picks(request):
    return render(request, 'top_picks.html')


def watched_movies(request):
    return render(request, 'watched_movies.html')


def logout_view(request):
    logout(request)
    return redirect('main')
