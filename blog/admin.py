# blog/admin.py
from django.contrib import admin
from .models import Post, Comment  # ← Commentをインポート

admin.site.register(Post)
admin.site.register(Comment)       # ← これを追加
