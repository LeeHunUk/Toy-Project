from memo.user.views import login_view, register, logout_view
from django.urls import path

urlpatterns = [
    path("", login_view, name="login"),
    path("register", register, name="register"),
    path("logout", logout_view, name="logout"),
]
