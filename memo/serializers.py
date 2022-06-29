from memo.models import Memos, Users, Labels
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


class MemoCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField(max_length=1000)
    writer = UserSerializer(read_only=True)
    img = serializers.FileField()

    def create(self, request, data, commit=True):
        instance = Memos()
        instance.writer_id = request.user.id
        instance.title = data.get("title")
        instance.content = data.get("content")
        instance.img = request.FILES['img']
        if commit:
            try:
                instance.save()
            except Exception as e:
                print(e)
            else:
                for i in request.POST.getlist("labels"):
                    instance.labels.add(Labels.objects.get(pk=i))

        return instance


class MemoSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField(max_length=1000)
    writer = UserSerializer(read_only=True)

    def update(self, data, pk, request, commit=True):
        instance = Memos.objects.get(pk=pk)
        instance.title = data.get('title')
        instance.content = data.get('content')
        if commit:
            try:
                instance.save()
            except Exception as e:
                print(e)
            else:
                pass

        return instance
