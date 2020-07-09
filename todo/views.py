from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy


from .models import TodoModel

# Create your views here.
class TodoList(ListView):
    template_name = 'list.html'
    #対象のテーブルを選択
    model = TodoModel


class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel


class TodoCreate(CreateView):
    template_name = 'create.html'
    #保存先のテーブルを選択
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    #データを作成したとき、redirectさせるviewを決める
    #クラス内ではreverse_lazy、関数内ではreverseを使用
    # success_url = reverse_lazy('list')
    # もしくはmodel(.py)でget_absolute_urlを指定する


class TodoDelete(DeleteView):
    template_name = 'delete.html'
    #対象のテーブルを選択
    model = TodoModel
    success_url = reverse_lazy('list')


class TodoUpdate(UpdateView):
    template_name = 'update.html'
    #対象のテーブルを選択
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')