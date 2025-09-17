from django.urls import path

from . import views

urlpatterns = [
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("", views.main, name="main"),
    path("advises", views.advised, name="advised"),
    path("top_picks", views.top_picks, name="top_picks"),
    path("watched_movies", views.watched_movies, name="watched_movies"),
    path('logout/', views.logout_func, name='logout'),




]
