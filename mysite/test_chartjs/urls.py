"This is a test program"
from django.urls import path

# STEP1: 現在のフォルダの「views.py」を import する！さっき編集したやつ！
from . import views

# STEP2: views.py には「index」という関数を作りましたね！それを呼んでます
urlpatterns = [
    # index.htmlがリクエストされたときは views.index の処理に
    path('', views.index, name='index'),
    # STEP3: いいね！がリクエストされたときは views.likes の処理に 引数[ユーザID, 記事ID] を渡します
    path('likes/<int:user_id>/<int:article_id>', views.likes, name='likes'),
]
