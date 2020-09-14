"""This is a test program"""
from django.db import models
from django.contrib.auth import get_user_model

# クラス名がテーブル名です
class DjangoTestTable(models.Model):
    """This is a test program"""
    # ここに定義したものがフィールド項目です
    month_code = models.CharField(default='XXX', max_length=3) # Jun Feb など
    sales = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

class Articles(models.Model):
    '''記事'''
    title = models.CharField(verbose_name='タイトル', max_length=200)
    note = models.TextField(verbose_name='投稿内容')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField('公開日時', auto_now_add=True)

class Likes(models.Model):
    '''いいね'''
    articles = models.ForeignKey('Articles', on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
