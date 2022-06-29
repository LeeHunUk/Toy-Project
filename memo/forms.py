from django import forms
from memo.models import Users, Labels
from argon2 import PasswordHasher, exceptions  # pip install argon2-cffi
from django.contrib.auth import login


class RegisterForm(forms.Form):
    user_id = forms.CharField(
        max_length=100, required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "아이디"})
    )

    password = forms.CharField(
        max_length=100, required=True,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "비밀번호", "minlength": 4})
    )

    password2 = forms.CharField(
        max_length=100, required=True,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "비밀번호 확인", "minlength": 4})
    )

    def save(self, user_id, pw1, pw2, request):
        user = Users.objects.filter(username=user_id)
        if user:
            msg = "이미 존재하는 유저입니다."
        elif pw1 != pw2:
            msg = "비밀번호가 일치하지 않습니다."
        else:
            msg = "회원가입이 완료되었습니다."
            u = Users(
                username=user_id,
                password=PasswordHasher().hash(pw1),
                user_auth="MEMBER")
            u.save()
            login(request, u)
        return msg


class LoginForm(forms.Form):
    user_id = forms.CharField(
        max_length=100, required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "아이디"})
    )

    password = forms.CharField(
        max_length=100, required=True,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "비밀번호"})
    )

    def login(self, user_id, pw):
        user = Users.objects.get(username=user_id)
        try:
            PasswordHasher().verify(user.password, pw)
        except exceptions.VerifyMismatchError:
            result = False
        else:
            result = True

        return result


class LabelForm(forms.Form):
    label = forms.CharField(
        max_length=100, required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "라벨을 등록해주세요."}))

    def save(self, keyword):
        labels = Labels.objects.filter(label=keyword)

        if labels:
            msg = "이미 존재하는 라벨입니다."
        else:
            msg = "등록이 완료되었습니다."
            u = Labels(label=keyword)
            u.save()

        return msg
