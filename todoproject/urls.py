from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
]


#adminにアクセスするためのUserを作成
#superuserはすべての管理者権限がある
#python manage.py createsuperuser
#admin.pyでadmin画面からデータを触れるようにする