from django.shortcuts import render
from django.views.generic import  ListView  , DetailView
from .models import MiddleTask , BottomTask

class IndexView(ListView):
    template_name="index.html"
    context_object_name="middle_task_list"
    model = MiddleTask
    # 単一のビューで複数表示
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'bottom_task_list': BottomTask.objects.order_by(),
        })
        return context
    
    def get_queryset(self):
        return MiddleTask.objects.order_by("delivery")
    
class TaskDetail(DetailView):
    template_name="post.html"
    model= MiddleTask