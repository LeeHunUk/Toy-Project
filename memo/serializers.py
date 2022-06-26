from memo.models import Memos, Users
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ["username", "date_joined", "last_login", "user_auth"]


class MemoListSerializer(serializers.ModelSerializer):
    writer = UserSerializer(read_only=True)

    class Meta:
        model = Memos
        fields = "__all__"
