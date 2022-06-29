from memo.models import Memos, Labels
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import MemoListSerializer, MemoSerializer, MemoCreateSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.http.response import Http404

from rest_framework.decorators import action, renderer_classes
from django.shortcuts import redirect, render
from memo.utils import MsgOk


class MemoViewSet(viewsets.ModelViewSet):
    queryset = Memos.objects.order_by("-created_at")
    serializer_class = MemoListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        # POST METHOD
        serializer = MemoCreateSerializer(data=request.data)

        if serializer.is_valid():
            rtn = serializer.create(request, serializer.data)
            print(rtn)

            return redirect('m_read')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        # Detail GET
        queryset = self.get_queryset().filter(pk=pk).first()
        serializer = MemoListSerializer(queryset)

        return Response(serializer.data)

    def update(self, request, pk=None):
        # PUT METHOD
        serializer = MemoSerializer(data=request.data)
        if serializer.is_valid():
            rtn = serializer.update(serializer.data, pk, request)
            return Response(MemoListSerializer(rtn).data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        # GET ALL
        queryset = self.get_queryset().all()
        serializer = MemoListSerializer(queryset, many=True)

        # 참고 사항
        # content = JSONRenderer().render(serializer.data)
        # stream = io.BytesIO(content)
        # data = JSONParser().parse(stream)

        return Response(serializer.data)

    @renderer_classes([JSONRenderer])
    def destroy(self, request, pk=None):
        # DELETE METHOD
        queryset = self.get_queryset().filter(pk=pk)
        if not queryset.exists():
            raise Http404
        queryset.delete()

        return MsgOk()

    @action(detail=True, methods=["get", "post"])
    def add_click(self, request, pk=None):
        queryset = self.get_queryset().filter(pk=pk)

        if not queryset.exists():
            raise Http404
        rtn = queryset.first().clicked()
        serializer = MemoListSerializer(rtn)

        return Response(status=status.HTTP_201_CREATED)
