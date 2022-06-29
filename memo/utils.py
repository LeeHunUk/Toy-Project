from rest_framework.response import Response

from memo.models import Memos
from django.db.models import F


def like_up(memo_id):
    count_number = 1
    Memos.objects.filter(pk=memo_id).update(like=F('like') + count_number)


def view_up(memo_id):
    count_number = 1
    Memos.objects.filter(pk=memo_id).update(view=F('view') + count_number)


def MsgOk(status: int = 200):
    return Response({"msg": "ok"}, status=status)
