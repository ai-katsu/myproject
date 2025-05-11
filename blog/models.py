from django.db import models

# 投稿を表すモデル（Post = ブログ記事）
class Post(models.Model):
    # 投稿タイトル（最大100文字）
    title = models.CharField(max_length=100)

    # 投稿本文（文字数制限なし）
    content = models.TextField()

    # 投稿日時（投稿時に自動でセットされる）
    created_at = models.DateTimeField(auto_now_add=True)

    # 管理画面などで表示されるタイトル文字列
    def __str__(self):
        return self.title
class Comment(models.Model):
    # Postモデルとの1対多の関係（1つの投稿に複数コメント可）
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    author = models.CharField(max_length=50)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author}: {self.text[:20]}"
    
    