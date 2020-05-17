from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            print('통과')
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        print('실패')
        form = CreateUserForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/form.html', context)

def login(request):
#    if request.user.is_athenticated:
#        return redirect('articles:index')
    if request.method=='POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')


def info(request, username):
    User = get_user_model()
    user = get_object_or_404(User, username=username)
    context = {
        'user':user,
    }
    return render(request,'accounts/info.html', context)


@login_required
def follow(request, username):
    User = get_user_model()
    user = get_object_or_404(User, username=username)
    if user!= request.user:
        if user.followers.filter(username=request.user.username).exists():
            user.followers.remove(request.user)
        else:
            user.followers.add(request.user)

    return redirect('accounts:info', user.username)