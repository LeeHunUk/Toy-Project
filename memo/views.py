from django.shortcuts import render
from memo.models import Labels, Memos
from django.core.paginator import Paginator


def index(request):

    labels = Labels.objects.all()
    like = Memos.objects.order_by("-like")
    view = Memos.objects.order_by("-view")

    like_paginator = Paginator(like, 6)
    like = like_paginator.get_page(1)

    view_paginator = Paginator(view, 6)
    view = view_paginator.get_page(1)

    best = (
        Memos.objects.order_by("-view")[0],
        Memos.objects.order_by("-like")[0])

    return render(request, "main.html", {"labels": labels, "like": like, "view": view})
