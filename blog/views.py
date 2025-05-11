# Djangoのrender関数をインポート
from django.shortcuts import render
# Postモデルをインポート
from .models import Post
# render関数とget_object_or_404関数をインポート
from django.shortcuts import render, get_object_or_404
# PostモデルとCommentモデルをインポート
from .models import Post, Comment

# トップページのビュー関数
def index(request):
    # Postモデルの全ての投稿を取得し、作成日時の降順で並べ替える
    posts = Post.objects.all().order_by('-created_at')
    
    # 'blog/index.html' テンプレートをレンダリングし、postsをコンテキストとして渡す
    return render(request, 'blog/index.html', {'posts': posts})


# 投稿の詳細ページを表示するビュー関数
def post_detail(request, post_id):
    # 指定されたpost_idに対応するPostオブジェクトを取得（見つからなければ404エラーを返す）
    post = get_object_or_404(Post, id=post_id)
    
    # 対象の投稿に紐づくコメントを作成日時の降順で取得
    comments = Comment.objects.filter(post=post).order_by('-created_at')
    
    # 'blog/post_detail.html' テンプレートをレンダリングし、投稿とコメントを渡す
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments
    })
