from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from django.views.decorators.http import require_http_methods, require_POST, require_GET


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

# @require_http_methods(['GET', 'POST'])
# def update(request, user_pk):
#     user = get_object_or_404(get_user_model(), pk=user_pk)
#     if request.method == 'POST':
#         form = CustomUserChangeForm(request.POST, request.FILES, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('movies:index')
    
#     else:
#         form = CustomUserChangeForm(instance=user)
#     context = {
#         'form': form,
#     }
#     return render(request, 'accounts/update.html', context)


# @require_POST
# def delete(request, user_pk):
#     user = get_object_or_404(get_user_model(), pk=user_pk)
#     user.delete()
#     return redirect('movies:index')

