from django.shortcuts import HttpResponseRedirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import File
from .forms import AddFileForm, LoginForm, SignUpForm


@login_required
def show_files(request):
    files = File.objects.filter(user=request.user)
    return render(request, 'show_files.html', {'user': request.user, 'files': files})


@login_required
def add_file(request):
    user = request.user
    if request.method == 'POST':
        form = AddFileForm(user, request.POST)
        if form.is_valid():
            data = form.cleaned_data
            File.objects.create(
                name=data['name'],
                parent=data['parent'],
                folder=data['folder'],
                user=user
            )
            return HttpResponseRedirect('/')
    else:
        form = AddFileForm(user)
    return render(request, 'add_file.html', {'form': form})


def add_user(request):
    if request.user.is_authenticated:
        logout(request)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            username = data.get('username')
            email = data.get('email')
            raw_password = data.get('password1')
            new_user = authenticate(username=username, password=raw_password)
            login(request, new_user)
        return HttpResponseRedirect('/')
    else:
        form = SignUpForm()
    return render(request, 'add_user.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
        if user:
            login(request, user)
        return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
