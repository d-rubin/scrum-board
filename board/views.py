from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/board')
        else:
            return render(request, 'login/login.html', {'invalid': True})
    return render(request, 'login/login.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/board')
        else:
            return render(request, 'register/register.html', {'form': form})
    form = UserCreationForm()
    return render(request, 'register/register.html', {'form': form})


def logout_view(request):
    logout(request)


def board_view(request):
    if request.user.is_authenticated:
        return render(request, 'board/board.html', {'first_name': request.user.first_name})
    return render(request, 'login/login.html')
