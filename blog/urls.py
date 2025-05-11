# Djangoのpath関数をインポート
from django.urls import path

# 同じアプリケーション内のviewsモジュールをインポート
from . import views

# URLパターンのリストを定義
urlpatterns = [
    # ルートURL（例: /blog/）にアクセスがあった場合、views.indexを実行
    # 'post_index' という名前をこのURLパターンに付けて、テンプレートやリダイレクトで参照できるようにする
    path('', views.index, name='post_index'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),  # ← 追加
]
