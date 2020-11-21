import requests

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_GET

from .models import Movie, MovieComment, UserScore
from accounts.models import User, UserFavoriteMovie, UserSimilarMovie

from .forms import MovieCommentForm, UserScoreForm

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


@require_GET
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user_score_form = UserScoreForm()
    movie_comment_form = MovieCommentForm()
    movie_comments = movie.moviecomment_set.all()
    user_movie_score = request.user.userscore_set.filter(user=request.user)
    context = {
        'movie': movie,
        'user_score_form': user_score_form,
        'movie_comment_form': movie_comment_form,
        'movie_comments': movie_comments,
        'user_movie_score': user_movie_score,
    }
    return render(request, 'movies/detail.html', context)


@require_POST
def movie_create_comment(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    movie_comment_form = MovieCommentForm(request.POST)
    if movie_comment_form.is_valid():
        movie_comment = movie_comment_form.save(commit=False)
        movie_comment.movie = movie
        movie_comment.user = request.user
        movie_comment.save()
        return redirect('movies:detail', movie.pk)

    context = {
        'movie': movie,
        'movie_comment_form': movie_comment_form,
    }
    return render(request, 'movies:detail.html', context)


@require_POST
def movie_delete_comment(request, movie_pk, comment_pk):
    movie_comment = get_object_or_404(MovieComment, pk=comment_pk)
    movie_comment.delete()
    return redirect('movies:detail', movie_pk)


def save_user_score(request, movie_pk):
    # 해당 영화에 평점을 남긴것만 반영되어야 하는데 모든 영화에 반영됨....
    movie = get_object_or_404(Movie, pk=movie_pk)
    # 이미 평가한 유저이면 수정 아니면 생성
    cur_eval_user = list(UserScore.objects.all().values('user'))
    # print(cur_eval_user)
    # print(request.user.id)
    user_score_form = UserScoreForm(request.POST)
    if user_score_form.is_valid():
        user_score = user_score_form.save(commit=False)
        user_score.user = request.user
        user_score.movie_id = movie.movie_id

        # 이미 평가한 유저인지 처음 평가한 유저인지에 따라 분기
        for i in range(len(cur_eval_user)):
            if cur_eval_user[i]['user'] == request.user.id:
                cur_user_score = get_object_or_404(UserScore, user=request.user)
                cur_user_score.score = user_score.score
                cur_user_score.save()
                break
        else:
            user_score.save()


        # user_score.score가 4점 이상이면 userfavorite에 해당 영화 정보 저장

        return redirect('movies:detail', movie.pk)

    context = {
        'movie': movie,
        'user_score_form': user_score_form,
    }
    return render(request, 'movies:detail.html', context)


@require_POST
def delete_user_score(request, movie_pk):
    user_movie_score = request.user.userscore_set.filter(user=request.user)
    user_movie_score.delete()
    
    return redirect('movies:detail', movie_pk)
    



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
    


        



    