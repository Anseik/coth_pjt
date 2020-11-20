import requests

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_GET

from .models import Movie
from accounts.models import User, UserFavoriteMovie, UserSimilarMovie

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
                movie.movie_id = result['id']
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
                movie.movie_id = result['id']
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


def similar(request, movie_pk):
    user = request.user
    cur_user_similar_movies_title = user.usersimilarmovie_set.all().values('title')
    movie = get_object_or_404(Movie, pk=movie_pk)

    url_similar = f'https://api.themoviedb.org/3/movie/{movie.movie_id}/similar'

    payload = {
        'api_key': 'c786a622d66f3b488b2035f1808f07d7',
        'language': 'ko-kr',
        'page': 1,
    }

    response = requests.get(url_similar, params=payload)
    similar_movies_dict = response.json()
    # print(similar_movies_dict)

    result = sorted(similar_movies_dict['results'], key=lambda x: -x['vote_average'])[:5]
    # print(result)

    for i in range(len(result)):
        # 인스턴스 생성
        usersimilarmovie = UserSimilarMovie()

        # 인스턴스 값 채우고 저장
        usersimilarmovie.popularity = result[i]['popularity']
        usersimilarmovie.vote_count = result[i]['vote_count']
        usersimilarmovie.video = result[i]['video']
        usersimilarmovie.poster_path = result[i]['poster_path']
        usersimilarmovie.movie_id = result[i]['id']
        usersimilarmovie.original_language = result[i]['original_language']
        usersimilarmovie.original_title = result[i]['original_title']
        usersimilarmovie.genre_ids = result[i]['genre_ids']
        usersimilarmovie.title = result[i]['title']
        usersimilarmovie.vote_average = result[i]['vote_average']
        usersimilarmovie.overview = result[i]['overview']
        usersimilarmovie.release_date = result[i]['release_date']
        usersimilarmovie.user = user

        check_title = {
            'title': usersimilarmovie.title,
        }

        if not check_title in cur_user_similar_movies_title:
            usersimilarmovie.save()

    return redirect('movies:index')
    


        



    