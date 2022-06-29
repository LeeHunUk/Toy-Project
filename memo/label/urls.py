from memo.label.views import label_create
from django.urls import path

urlpatterns = [
    path("create", label_create, name="l_create"),
]
