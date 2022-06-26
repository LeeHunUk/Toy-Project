from django.contrib import admin
from memo.models import Users, Memos, Labels, Chats

# Register your models here.
admin.site.register(Users)
admin.site.register(Memos)
admin.site.register(Labels)
admin.site.register(Chats)
