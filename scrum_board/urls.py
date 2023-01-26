from django.contrib import admin
from django.urls import path

from board.views import board, register_request, login_request, logout_request

urlpatterns = [
    path("", login_request, name="login"),
    path("login/", login_request, name="login"),
    path('admin/', admin.site.urls),
    path('board/', board),
    path("register/", register_request, name="register"),
    path("logout/", logout_request, name="logout"),
]
