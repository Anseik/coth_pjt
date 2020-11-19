from django.shortcuts import render, redirect, get_object_or_404
from .models import ReviewArticle, ReviewComment, TalkArticle, TalkComment
from .forms import ReviewArticleForm, ReviewCommentForm, TalkArticleForm, TalkCommentForm
from django.views.decorators.http import require_http_methods, require_POST, require_GET
from django.contrib.auth.decorators import login_required

# review
@require_GET
def review_index(request):
    reviews = ReviewArticle.objects.order_by('-pk')
    context = {
        'reviews': reviews,
    }
    return render(request, 'articles/review_index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def review_create(request):
    if request.method == 'POST':
        form = ReviewArticleForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('articles:review_index')

    else:
        form = ReviewArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/review_create.html', context)        


@require_GET
def review_detail(request, review_pk):
    review = get_object_or_404(ReviewArticle, pk=review_pk)
    review_comment_form = ReviewCommentForm()
    review_comments = review.reviewcomment_set.all()
    # rank = ('★' * review.rank) + '☆' * (5 - review.rank)
    context = {
        'review': review,
        'review_comment_form': review_comment_form,
        'review_comments': review_comments,
        # 'rank': rank,
    }
    return render(request, 'articles/review_detail.html', context)


@require_http_methods(['GET', 'POST'])
def review_update(request, review_pk):
    review = get_object_or_404(ReviewArticle, pk=review_pk)
    if request.method == 'POST':
        form = ReviewArticleForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            return redirect('articles:review_detail', review.pk)

    else:
        form = ReviewArticleForm(instance=review)
    context = {
        'form': form,
    }
    return render(request, 'articles/review_update.html', context)    


@require_POST
def review_delete(request, review_pk):
    review = get_object_or_404(ReviewArticle, pk=review_pk)
    review.delete()
    return redirect('articles:review_index')


@require_POST
def review_create_comment(request, review_pk):
    review = get_object_or_404(ReviewArticle, pk=review_pk)
    review_comment_form = ReviewCommentForm(request.POST)
    if review_comment_form.is_valid():
        review_comment = review_comment_form.save(commit=False)
        review_comment.review_article = review
        review_comment.user = request.user
        review_comment.save()
        return redirect('articles:review_detail', review.pk)

    context = {
        'review': review,
        'comment_form': comment_form,
    }
    return render(request, 'articles/review_detail.html', context)


@require_POST
def review_delete_comment(request, review_pk, comment_pk):
    review_comment = get_object_or_404(ReviewComment, pk=comment_pk)
    review_comment.delete()
    return redirect('articles:review_detail', review_pk)



# talk
@require_GET
def talk_index(request):
    talks = TalkArticle.objects.order_by('-pk')
    context = {
        'talks': talks,
    }
    return render(request, 'articles/talk_index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def talk_create(request):
    if request.method == 'POST':
        form = TalkArticleForm(request.POST, request.FILES)
        if form.is_valid():
            talk = form.save(commit=False)
            talk.user = request.user
            talk.save()
            return redirect('articles:talk_index')

    else:
        form = TalkArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/talk_create.html', context)


@require_GET
def talk_detail(request, talk_pk):
    talk = get_object_or_404(TalkArticle, pk=talk_pk)
    talk_comment_form = TalkCommentForm()
    talk_comments = talk.talkcomment_set.all()
    context = {
        'talk': talk,
        'talk_comment_form': talk_comment_form,
        'talk_comments': talk_comments,
    }
    return render(request, 'articles/talk_detail.html', context)


@require_http_methods(['GET', 'POST'])
def talk_update(request, talk_pk):
    talk = get_object_or_404(TalkArticle, pk=talk_pk)
    if request.method == 'POST':
        form = TalkArticleForm(request.POST, request.FILES, instance=talk)
        if form.is_valid():
            form.save()
            return redirect('articles:talk_detail', talk.pk)

    else:
        form = TalkArticleForm(instance=talk)
    context = {
        'form': form,
    }
    return render(request, 'articles/talk_update.html', context)


@require_POST
def talk_delete(request, talk_pk):
    talk = get_object_or_404(TalkArticle, pk=talk_pk)
    talk.delete()
    return redirect('articles:talk_index')


@require_POST
def talk_create_comment(request, talk_pk):
    talk = get_object_or_404(TalkArticle, pk=talk_pk)
    talk_comment_form = TalkCommentForm(request.POST)
    if talk_comment_form.is_valid():
        talk_comment = talk_comment_form.save(commit=False)
        talk_comment.talk_article = talk
        talk_comment.user = request.user
        talk_comment.save()
        return redirect('articles:talk_detail', talk.pk)

    context = {
        'talk': talk,
        'talk_comment_form': talk_comment_form,
    }
    return render(request, 'articles/talk_detail.html', context)


@require_POST
def talk_delete_comment(request, talk_pk, comment_pk):
    talk_comment = get_object_or_404(TalkComment, pk=comment_pk)
    talk_comment.delete()
    return redirect('articles:talk_detail', talk_pk)