import requests

from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_GET

from .models import Movie

# Create your views here.
@require_POST
def savedata(request):
    movie_titles = Movie.objects.all().values('title')
    # print(movie_titles)

    # https://api.themoviedb.org/3/movie/popular?api_key=c786a622d66f3b488b2035f1808f07d7&language=ko-kr&page=1
    if request.user.is_superuser:
        url_popular = 'https://api.themoviedb.org/3/movie/popular'
        url_top = 'https://api.themoviedb.org/3/movie/top_rated'

        for page in range(1, 6):
            payload = {
                'api_key': 'c786a622d66f3b488b2035f1808f07d7',
                'language': 'ko-kr',
                'page': page,
            }

            response = requests.get(url_popular, params=payload)
            movies_dict = response.json()
            # print(movies_dict['results'][0]['title'])
            for i in range(len(movies_dict['results'])):
                movie = Movie()
                result = movies_dict['results'][i]

                movie.popularity = result['popularity']
                movie.vote_count = result['vote_count']
                movie.video = result['video']
                movie.poster_path = result['poster_path']
                movie.original_language = result['original_language']
                movie.original_title = result['original_title']
                movie.genre_ids = result['genre_ids']
                movie.title = result['title']
                movie.vote_average = result['vote_average']
                movie.overview = result['overview']
                movie.release_date = result['release_date']

                check_title = {
                    'title': movie.title,
                }

                if not check_title in movie_titles:
                    movie.save()

            
            response = requests.get(url_top, params=payload)
            movies_dict = response.json()
            # print(movies_dict['results'][0]['title'])
            for i in range(len(movies_dict['results'])):
                movie = Movie()
                result = movies_dict['results'][i]

                movie.popularity = result['popularity']
                movie.vote_count = result['vote_count']
                movie.video = result['video']
                movie.poster_path = result['poster_path']
                movie.original_language = result['original_language']
                movie.original_title = result['original_title']
                movie.genre_ids = result['genre_ids']
                movie.title = result['title']
                movie.vote_average = result['vote_average']
                movie.overview = result['overview']
                movie.release_date = result['release_date']

                check_title = {
                    'title': movie.title,
                }

                if not check_title in movie_titles:
                    movie.save()            
                
    return redirect('movies:index')


@require_POST
def deletedata(request):
    if request.user.is_superuser:
        Movie.objects.all().delete()

    return redirect('movies:index')


def index(request):
    movies = Movie.objects.all()
    top_movies = Movie.objects.order_by('-vote_average')[:10]

    context = {
        'movies': movies,
        'top_movies': top_movies,
    }
    return render(request, 'movies/index.html', context)