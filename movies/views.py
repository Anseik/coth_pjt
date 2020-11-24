import requests
import json

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_GET
from django.db.models import Q

from .models import Movie, MovieComment, UserScore, Genre, MovieGenre
from accounts.models import User, UserFavoriteMovie, UserSimilarMovie

from .forms import MovieCommentForm, UserScoreForm

from django.http import JsonResponse


genre_dict = {
    12: '모험',         
    14: '판타지',         
    16: '애니메이션',         
    18: '드라마',         
    27: '공포',         
    28: '액션',         
    35: '코미디',         
    36: '역사',         
    37: '서부',         
    53: '스릴러',         
    80: '범죄',
    99: '다큐멘터리',
    878: 'SF',
    9648: '미스터리',
    10402: '음악',
    10749: '로맨스',
    10751: '가족',
    10752: '전쟁',
    10770: 'TV 영화',
}

# Create your views here.
@require_GET
def first(request):
    return render(request, 'first.html')


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
                
                    genres = list(movie.genre_ids)
                    for genre in genres:
                        genre_instance = get_object_or_404(Genre, pk=genre)
                        # print(genre_instance)
                        moviegenre = MovieGenre()
                        moviegenre.movie = movie
                        moviegenre.genre = genre_instance
                        moviegenre.save()

            
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
                    
                    genres = list(movie.genre_ids)
                    for genre in genres:
                        genre_instance = get_object_or_404(Genre, pk=genre)
                        # print(genre_instance)
                        moviegenre = MovieGenre()
                        moviegenre.movie = movie
                        moviegenre.genre = genre_instance
                        moviegenre.save()
                
    return redirect('movies:index')


@require_POST
def deletedata(request):
    if request.user.is_superuser:
        Movie.objects.all().delete()

    return redirect('movies:index')


@require_POST
def save_genres(request):
    genres_name = Genre.objects.all().values('name')
    if request.user.is_superuser:
        url_genre = 'https://api.themoviedb.org/3/genre/movie/list'

        payload = {
            'api_key': 'c786a622d66f3b488b2035f1808f07d7',
            'language': 'ko-kr',
        }

        response = requests.get(url_genre, params=payload)
        genres_dict = response.json()
        # print(genres_dict['genres'])
        result = genres_dict['genres']
        for i in range(len(result)):
            genre = Genre()
            genre.genre_id = result[i]['id']
            genre.name = result[i]['name']

            check_name = {
                'name': genre.name,
            }

            if not check_name in genres_name:
                genre.save()

    return redirect('movies:index')


@require_POST
def delete_genres(request):
    genres = Genre.objects.all()
    if request.user.is_superuser:
        genres.delete()

    return redirect('movies:index')


@require_GET
def index(request):
    user = request.user
    movies = Movie.objects.order_by('-vote_average')[:24]
    top_movies = Movie.objects.order_by('-vote_average')[:10] # top10
    date_movies  = Movie.objects.order_by('-release_date')[:10] # 최신영화

    # 로그인된 유저일 경우
    if request.user.is_authenticated:
        mytype_movies = user.usersimilarmovie_set.all().order_by('-vote_average')[:10]
        popularity_movies = Movie.objects.order_by('-popularity')[:10]
        dibs_movies = user.dibs_movies.order_by('-vote_average')[:10]
        vote_count_movies = Movie.objects.order_by('-vote_count')[:10]
        # 선호 장르
        prefer1_movieid = MovieGenre.objects.filter(genre=user.genre_prefer1).values('movie')
        prefer2_movieid = MovieGenre.objects.filter(genre=user.genre_prefer2).values('movie')
        prefer3_movieid = MovieGenre.objects.filter(genre=user.genre_prefer3).values('movie')
        prefer1_movies = Movie.objects.filter(id__in=prefer1_movieid).order_by('-vote_average')[:8]
        prefer2_movies = Movie.objects.filter(id__in=prefer2_movieid).order_by('-vote_average')[:8]
        prefer3_movies = Movie.objects.filter(id__in=prefer3_movieid).order_by('-vote_average')[:8]

        genre_prefer1 = genre_dict[user.genre_prefer1]
        genre_prefer2 = genre_dict[user.genre_prefer2]
        genre_prefer3 = genre_dict[user.genre_prefer3]

        # print(genre_prefer1)
        # print(genre_prefer2)
        # print(genre_prefer3)

        context = {
            'movies': movies,
            'date_movies': date_movies,
            'top_movies': top_movies,
            'mytype_movies': mytype_movies,
            'popularity_movies': popularity_movies,
            'dibs_movies': dibs_movies,
            'vote_count_movies': vote_count_movies,
            'prefer1_movies': prefer1_movies,
            'prefer2_movies': prefer2_movies,
            'prefer3_movies': prefer3_movies,
            'genre_prefer1': genre_prefer1,
            'genre_prefer2': genre_prefer2,
            'genre_prefer3': genre_prefer3,
        }
        return render(request, 'movies/index.html', context)        

    # 로그인하지 않은 유저일 경우
    else:
        popularity_movies = Movie.objects.order_by('-popularity')[:10]
        vote_count_movies = Movie.objects.order_by('-vote_count')[:10]

        context = {
            'movies': movies,
            'date_movies': date_movies,
            'top_movies': top_movies,
            'popularity_movies': popularity_movies,
            'vote_count_movies': vote_count_movies,
        }
        return render(request, 'movies/index.html', context)          


@require_GET
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user_score_form = UserScoreForm()
    movie_comment_form = MovieCommentForm()
    movie_comments = movie.moviecomment_set.all()
    if request.user.is_authenticated:
        user_movie_score = request.user.userscore_set.filter(user=request.user).filter(movie_origin_id=movie.movie_id)
    else:
        user_movie_score = []

    genres = json.loads(movie.genre_ids)
    # print(genres)
    genres_name = []
    for genre in genres:
        genres_name.append(genre_dict[genre])
    # print(genres_name)
   
    context = {
        'movie': movie,
        'user_score_form': user_score_form,
        'movie_comment_form': movie_comment_form,
        'movie_comments': movie_comments,
        'user_movie_score': user_movie_score,
        'genres_name': genres_name,
    }
    return render(request, 'movies/detail.html', context)


@require_POST
def movie_create_comment(request, movie_pk):
    if request.user.is_authenticated:
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
    else:
        return redirect('accounts:login')


@require_POST
def movie_delete_comment(request, movie_pk, comment_pk):
    movie_comment = get_object_or_404(MovieComment, pk=comment_pk)
    if request.user == movie_comment.user:
        movie_comment.delete()
    return redirect('movies:detail', movie_pk)



def save_user_score(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    # 이미 평가한 유저이면 수정 아니면 생성
    cur_eval_user = list(UserScore.objects.filter(movie_origin_id=movie.movie_id).values('user'))
    # print(cur_eval_user)
    # print(request.user.id)
    user_score_form = UserScoreForm(request.POST)
    if user_score_form.is_valid():
        user_score = user_score_form.save(commit=False)
        user_score.user = request.user
        user_score.movie = movie
        user_score.movie_origin_id = movie.movie_id

        # 이미 평가한 유저인지 처음 평가한 유저인지에 따라 분기
        for i in range(len(cur_eval_user)):
            if cur_eval_user[i]['user'] == request.user.id:
                cur_user_score = get_object_or_404(UserScore, user=request.user, movie_origin_id=movie.movie_id)
                # print(cur_user_score)
                cur_user_score.score = user_score.score
                cur_user_score.save()
                break
        else:
            user_score.save()


        # user_score.score가 4점 이상이면 userfavorite에 해당 영화 정보 저장
        if user_score.score >= 4:
            similar(request, movie_pk)
        
        return redirect('movies:detail', movie.pk)

    context = {
        'movie': movie,
        'user_score_form': user_score_form,
    }
    return render(request, 'movies:detail.html', context)


@require_POST
def delete_user_score(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user_movie_score = request.user.userscore_set.filter(user=request.user).filter(movie_origin_id=movie.movie_id)
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

    result = sorted(similar_movies_dict['results'], key=lambda x: -x['vote_average'])[:10]
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


@require_GET
def mytype_movie(request):
    if request.user.is_authenticated:
        mytype_movies = request.user.usersimilarmovie_set.all()

        context = {
            'mytype_movies': mytype_movies,    
        }
        return render(request, 'movies/mytype.html', context)
    return redirect('accounts:login')


@require_GET
def mytype_detail(request, movie_pk):
    movie = get_object_or_404(UserSimilarMovie, pk=movie_pk)
    genres = json.loads(movie.genre_ids)
    # print(genres)
    genres_name = []
    for genre in genres:
        genres_name.append(genre_dict[genre])
    # print(genres_name)
   
    context = {
        'movie': movie,
        'genres_name': genres_name,
    }
    return render(request, 'movies/mytype_detail.html', context)


@require_POST
def dibs_movie(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = request.user

        if movie.dibs_users.filter(pk=user.pk).exists():
        # if user in article.like_users.all():
            movie.dibs_users.remove(user)
            dibed = False
        else:
            movie.dibs_users.add(user)
            dibed = True
            
        count = movie.dibs_users.count()

        context = {
            'dibed': dibed,
            'count': count,
        }

        return JsonResponse(context)
    return redirect('accounts:login')


@require_GET
def mydibs_movie(request, user_pk):
    if request.user.is_authenticated:
        user = request.user
        mydibs_movies = user.dibs_movies.all()
        # print(mydibs_movies)

        context = {
            'mydibs_movies': mydibs_movies,
        }

        return render(request, 'movies/mydibs_movies.html', context)
    return redirect('accounts:login')


@require_GET
def new_movies(request):
    new_movies = Movie.objects.order_by('-release_date')[:20]

    context = {
        'new_movies': new_movies,
    }

    return render(request, 'movies/new_movies.html', context)


@require_GET
def search(request):
    searchword = request.GET.get('searchword')
    if not searchword:
        search_movies = []
    else:
        search_movies = Movie.objects.filter(Q(title__icontains=searchword)|Q(overview__icontains=searchword))
    
    context = {
        'search_movies': search_movies,
    }

    return render(request, 'movies/search.html', context)


    


        



    