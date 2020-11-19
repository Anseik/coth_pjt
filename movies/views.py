import requests
from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def getdata(request):

    # https://api.themoviedb.org/3/movie/popular?api_key=c786a622d66f3b488b2035f1808f07d7&language=ko-kr&page=1
    if request.user.is_superuser:
        url = 'https://api.themoviedb.org/3/movie/popular'

        for page in range(1, 6):
            payload = {
                'api_key': 'c786a622d66f3b488b2035f1808f07d7',
                'language': 'ko-kr',
                'page': page,
            }

            response = requests.get(url, params=payload)
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

                movie.save()
                
    return redirect('movies:index')


def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)