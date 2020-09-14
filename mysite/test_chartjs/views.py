''' This project is test'''
from django.shortcuts import render # 追加！
from sqlalchemy import create_engine
import pandas as pd
from django.http import JsonResponse
from .models import DjangoTestTable # 追加！
from .models import Likes, Articles

def index(request):
    # 日付を降順に表示するクエリ
    ret = DjangoTestTable.objects.order_by('-pub_date')

    # （追加ここから）
    # mysql
    con_str = 'mysql+mysqldb://python:python123@127.0.0.1/db?charset=utf8&use_unicode=1'
    con = create_engine(con_str, echo=False).connect()

    # likes
    user_id = 1 # todo: where user_id
    articles = pd.read_sql_query(
        '''
        SELECT a.id, a.title, a.note, COALESCE(qry1.is_like, 0) is_like, qry2.likes_cnt
        FROM test_chartjs_articles a
            LEFT JOIN (
                SELECT articles_id, 1 is_like
                FROM test_chartjs_likes WHERE user_id = {0}) qry1 ON a.id = qry1.articles_id
            LEFT JOIN (
                SELECT articles_id, COUNT(user_id) likes_cnt
                FROM test_chartjs_likes GROUP BY articles_id) qry2 ON a.id = qry2.articles_id
        ORDER BY a.id;
        '''.format(user_id), con)
    # （追加ここまで）

    context = {
       'latest_list': ret,
       'articles': articles,
   }

    # htmlとして返却します
    return render(request, 'test_chartjs/index.html', context)

    # ここから↓を全部追加
def likes(request, user_id, article_id):
    """いいねボタンをクリック"""
    if request.method == 'POST':
        query = Likes.objects.filter(user_id=user_id, articles_id=article_id)
        if query.count() == 0:
            likes_tbl = Likes()
            likes_tbl.user_id = user_id
            likes_tbl.articles_id = article_id
            likes_tbl.save()
        else:
            query.delete()

        # response json
        return JsonResponse({"status": "responded by views.py"})
