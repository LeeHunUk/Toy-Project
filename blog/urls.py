"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from memo.views import index, memo_create, memo_view, memo_retrieve, memo_update
from django.conf.urls.static import static
from django.conf import settings

# rest_framework
from rest_framework import routers
from memo.apis import *

router = routers.DefaultRouter()
router.register(r'memos', MemoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),

    path("memo", memo_create, name="m_create"),
    path("memo/list", memo_view, name="m_read"),
    path("memo/<int:memo_id>", memo_retrieve, name="m_retrieve"),
    path("update/<int:memo_id>", memo_update, name="m_update"),

    path("user/", include("memo.user.urls")),
    path("label/", include("memo.label.urls")),
    path("apis/", include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
