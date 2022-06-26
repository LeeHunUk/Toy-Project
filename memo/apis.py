from memo.models import Memos
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import MemoListSerializer
from rest_framework.response import Response


class MemoViewSet(viewsets.ModelViewSet):
    queryset = Memos.objects.order_by("-like")
    serializer_class = MemoListSerializer
    permission_classes = [permissions.IsAuthenticated]
