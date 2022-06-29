from django.shortcuts import render
from memo.models import Labels, Memos
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from memo.utils import like_up, view_up


def index(request):

    labels = Labels.objects.all()

    view = Memos.objects.order_by("-created_at")
    best = ()
    if view.count() >= 1:
        best = (Memos.objects.order_by("-view")
                [0], Memos.objects.order_by("-like")[0])

    view_paginator = Paginator(view, 9)
    view = view_paginator.get_page(1)

    return render(request, "main.html", {"labels": labels, "best": best, "view": view})


@login_required
def memo_create(request):
    labels = Labels.objects.all()

    return render(request, "memo/create.html", {"labels": labels})


@login_required
def memo_update(request, memo_id):

    view = Memos.objects.filter(pk=memo_id)
    labels = Labels.objects.all()

    return render(request, "memo/update.html", {"view": view, "labels": labels})


@login_required
def memo_view(request):
    page = int(request.GET.get("p", 1))

    view = Memos.objects.order_by("-created_at")

    view_paginator = Paginator(view, 12)
    view = view_paginator.get_page(page)

    return render(request, "memo/list.html", {"view": view})


@login_required
def memo_retrieve(request, memo_id):

    view = Memos.objects.filter(pk=memo_id)

    view_up(memo_id)

    return render(request, "memo/read.html", {"view": view})
