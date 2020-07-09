from django.db import models
from django.urls import reverse



PRIORITY = (('danger', 'high'), ('info', 'normal'), ('success', 'low'))

# Create your models here.
#TodoModelというテーブルを作る
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices = PRIORITY
    )
    #defaultではnull=False
    duedate = models.DateField()
    def __str__(self):
        #admin管理画面での表示を変える
        return self.title

    #データを作成したとき、redirectさせるviewを決める
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk':self.pk})   

#データベースとmodelsの中間の設計書を作成
#python manage.py makemigrations
#実際にデータねーすに書き込む
#python manage.py migrate