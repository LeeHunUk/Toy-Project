from django.shortcuts import render, redirect
from memo.models import Users
from memo.forms import LoginForm, RegisterForm
from django.contrib.auth import login, logout


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data.get("user_id")
            raw_password = form.cleaned_data.get("password")
            raw_password2 = form.cleaned_data.get("password2")
            msg = form.save(user_id, raw_password, raw_password2, request)

        return render(request, "user/register.html", {"form": form, "msg": msg})
    else:
        form = RegisterForm()
        return render(request, "user/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data.get("user_id")
            raw_password = form.cleaned_data.get("password")
            msg = "올바른 유저ID와 패스워드를 입력하세요."
            try:
                user = Users.objects.get(username=user_id)
            except Users.DoesNotExist:
                pass
            else:
                if form.login(user_id, raw_password):
                    msg = None
                    login(request, user)
                    return redirect(request.GET.get("next") or "index")
    else:
        msg = None
        form = LoginForm()
    return render(request, "user/login.html", {"form": form, "msg": msg})


def logout_view(request):
    logout(request)

    return redirect("login")
