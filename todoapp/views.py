from django.shortcuts import render
from django.views.generic import  ListView  , DetailView
from .models import MiddleTask , BottomTask
from django.core.paginator import Paginator
class IndexView(ListView):
    template_name="index.html"
    paginate_by=5
    
    model = BottomTask
    # 単一のビューで複数表示
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
        # コンテクスト拡張
        context.update({
            'bottom_task_list': BottomTask.objects.order_by("parent_task__id"),
            "middle_task_list": MiddleTask.objects.order_by("id")
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
        context['related_task'] = BottomTask.objects.filter(parent_task__id=self.kwargs['pk'])
        return context