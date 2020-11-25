from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

from django.views.decorators.http import require_http_methods, require_POST, require_GET

from django.http import JsonResponse

from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect ('movies:index')

    else: 
        form = CustomUserCreationForm
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('movies:index')

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'movies:index')

    else:
        form = AuthenticationForm()
    context = {
        'form' : form, 
    }
    return render(request, 'accounts/login.html', context)


@require_GET
def logout(request):
    auth_logout(request)
    return redirect('movies:index')


@require_http_methods(['GET', 'POST'])
def update(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    if request.user == user:
        if request.method == 'POST':
            form = CustomUserChangeForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                return redirect('accounts:profile', user.pk)
        
        else:
            form = CustomUserChangeForm(instance=user)
        context = {
            'form': form,
        }
        return render(request, 'accounts/update.html', context)
    return redirect(request, 'movies:index')


@require_http_methods(['GET', 'POST'])
def password_change(request, user_pk):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            return redirect('accounts:update', request.user.pk)
    else:
        form = PasswordChangeForm(request.user)
    context ={
        'form': form,
    }
    return render(request, 'accounts/password_change.html', context)


@require_POST
def delete(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    user.delete()
    return redirect('movies:index')


@require_GET
def profile(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)


@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=user_pk)
        user = request.user
        if person != user:
            if person.followers.filter(pk=user.pk).exists():
                person.followers.remove(user)
                follow = False
            else:
                person.followers.add(user)
                follow = True
            context = {
                'follow': follow,
                'followings_cnt': person.followings.count(),
                'followers_cnt': person.followers.count(),
            }
            return JsonResponse(context)
    return redirect('accounts:profile', person.pk)
