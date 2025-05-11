# Djangoによって自動生成されたマイグレーションファイル（バージョン5.2.1）
# 作成日時: 2025年5月10日 03:08

from django.db import migrations, models

# マイグレーションクラスの定義
class Migration(migrations.Migration):

    # このマイグレーションは初期状態（新しいアプリ）として扱われる
    initial = True

    # このマイグレーションに依存する他のマイグレーションはない
    dependencies = [
    ]

    # 実行されるマイグレーション操作の一覧
    operations = [
        # Postモデルのテーブルを作成
        migrations.CreateModel(
            name='Post',
            fields=[
                # IDフィールド（自動生成される主キー）
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                
                # タイトル（最大100文字）
                ('title', models.CharField(max_length=100)),
                
                # 本文（長文テキスト）
                ('content', models.TextField()),
                
                # 作成日時（レコード作成時に自動設定される）
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
