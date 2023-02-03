from django.shortcuts import render


def login_view(request):
    return render(request, 'board/board.html')


def register_view(request):
    pass


def logout_view(request):
    pass