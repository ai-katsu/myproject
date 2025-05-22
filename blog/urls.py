from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # ← Django標準のログインビュー

urlpatterns = [
    # 投稿関連のルーティング
    path('', views.index, name='post_index'),
    path('create/', views.post_create, name='post_create'), 
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('<int:post_id>/delete/', views.post_delete, name='post_delete'),
    path('comments/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),

    # 🔒 認証機能（ログイン・ログアウト・サインアップ）
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),   # ログイン画面
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),         # ログアウト処理
    path('signup/', views.signup, name='signup'),                                             # 新規登録画面（自作ビュー）
    path('home/', views.home, name='home'),

]
