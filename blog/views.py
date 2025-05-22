from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm

from .models import Post, Comment
from django.contrib.auth.decorators import login_required

# トップページのビュー関数
def index(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "blog/index.html", {"posts": posts})


# 投稿の詳細ページを表示するビュー関数
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post).order_by("-created_at")

    # 🔽 コメント投稿処理を追加
    if request.method == "POST":
        author = request.POST.get("author")
        text = request.POST.get("text")
        if author and text:
            Comment.objects.create(post=post, author=author, text=text)
        return redirect("post_detail", post_id=post.id)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post, "comments": comments},
    )


# 投稿作成ページのビュー関数
@login_required
def post_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Post.objects.create(title=title, content=content, author=request.user)
        return redirect("post_index")
    return render(request, "blog/post_form.html")

# 投稿の編集機能
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.save()
        return redirect("post_detail", post_id=post.id)

    return render(request, "blog/post_form.html", {"post": post})

# 投稿の削除機能
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        post.delete()
        return redirect("post_index")

    return render(request, "blog/post_confirm_delete.html", {"post": post})

def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post_id = comment.post.id
    if request.method == "POST":
        comment.delete()
    return redirect("post_detail", post_id=post_id)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # 登録後ログイン画面へ
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def home(request):
    return render(request, 'home.html')