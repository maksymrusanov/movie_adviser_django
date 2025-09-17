from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login


def main(request):
    if request.user.is_authenticated:
        return render(request, 'main.html')
    return render(request, 'main.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            return render(request, 'login_page.html', {'error': 'Invalid username or password'})

    return render(request, 'login_page.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(
            username=username, email=email, password=password)

        login(request, user)

        return redirect('main')

    return render(request, 'registration_page.html')


def advised(request):
    return render(request, 'movies_advised.html')


def top_picks(request):
    return render(request, 'top_picks.html')


def watched_movies(request):
    return render(request, 'watched_movies.html')


def logout_func(request):
    logout(request)
    return redirect('main')
