from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from memo.models import Labels
from memo.forms import LabelForm


@login_required
def label_create(request):
    if request.method == "POST":
        form = LabelForm(request.POST)
        if form.is_valid():
            label = form.cleaned_data.get("label")
            msg = form.save(label)

        return render(request, "label/create.html", {"form": form, "msg": msg})
    else:
        form = LabelForm()
    return render(request, "label/create.html", {"form": form})
