from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView , TemplateView

from accounts.forms import CustomUserCreationForm

class SignUpView(CreateView):
    # フォームの指定
    form_class = CustomUserCreationForm 
    template_name="signup.html"
    
    success_url=reverse_lazy("accounts:signup_success")
    
    def form_valid(self, form):
        user = form.save()
        self.object = user        
        return super().form_valid(form)
    
class SignUpSuccessView(TemplateView):
        template_name="signup_success.html"
        