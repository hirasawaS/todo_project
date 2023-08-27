from django.shortcuts import render
from django.views.generic import  ListView , DetailView , CreateView , UpdateView
from .models import MiddleTask , BottomTask
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from .forms  import ButtomTaskForm
from django.contrib import messages
from django import template
class IndexView(ListView):
    template_name="index.html"
    paginate_by=5
    
    model = BottomTask
    # 単一のビューで複数表示
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    # 文字を見やすく
        pre_bottom_data = BottomTask.objects.order_by("parent_task__id")
        pre_middle_data = MiddleTask.objects.order_by("id")
        
        for i in range(len(pre_bottom_data)):
            pre_bottom_data[i].description = replace_long_string(pre_bottom_data[i].description)
            
        for i in range(len(pre_middle_data)):
            pre_middle_data[i].description = replace_long_string(pre_middle_data[i].description)
        
        # コンテクスト拡張
        context.update({
            'bottom_task_list': pre_bottom_data , 
            "middle_task_list": pre_middle_data
        })
        
    # ページネーター指定
        paginator = Paginator(context['bottom_task_list'], self.paginate_by)
        page_number = self.request.GET.get('page' ,1 )
        page_obj = paginator.page(page_number)
        
        context.update({
            'page_obj': page_obj,
            'paginator': paginator,
        })
        return context

    
class TaskDetail(DetailView):
    template_name="detail.html"
    model= MiddleTask
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 表示を制限
        pre_related_data = BottomTask.objects.filter(parent_task__id=self.kwargs['pk'])
        
        for i in range(len(pre_related_data)):
            pre_related_data[i].description = replace_long_string(pre_related_data[i].description) 
        context['related_task'] = pre_related_data
        return context
    

class CreateBottomTaskView(CreateView):
    model = BottomTask
    template_name="task_create.html"
    form_class= ButtomTaskForm
        
    def get_success_url(self):
        return reverse_lazy("todoapp:detail" , kwargs={'pk' : self.object.parent_task.pk})
    
    def form_valid(self , form):
        bottom_task = form.save(commit=False)
        bottom_task.save()
        messages.success(self.request , "タスクを生成しました")
        return super().form_valid(form)
    
    def form_invalid(self , form):
        messages.error(self.request , "タスクを生成できませんでした")
        return super().form_invalid(form)
    

class BottomTaskUpdateView(UpdateView):
    model = BottomTask
    template_name = "task_update.html"
    form_class = ButtomTaskForm
    
    def get_success_url(self):
        return reverse_lazy("todoapp:detail" , kwargs={'pk' : self.object.parent_task.pk})
    
    def form_valid(self , form):
        bottom_task = form.save(commit=False)
        bottom_task.save()
        messages.success(self.request , "タスクを編集しました")
        return super().form_valid(form)
    
    def form_invalid(self , form):
        messages.error(self.request , "タスクを編集できませんでした")
        return super().form_invalid(form)

# フィルター各種
register = template.Library()
@register.filter
def replace_long_string(s: str) -> str:
    if len(s) > 100:
        return s[0:50] + "・・・"
    else:
        return s