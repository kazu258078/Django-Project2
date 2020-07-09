from django.contrib import admin
from .models import TodoModel

# Register your models here.
#admin画面でTodoModelのデータを扱えるようにする
admin.site.register(TodoModel)