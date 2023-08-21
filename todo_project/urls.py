from django.contrib import admin
from django.urls import path , include
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path("" , include("todoapp.urls")) ,
    path("" , include("accounts.urls")),
    
# パスワードリセット申し込み
    path("password_reset/" , auth_view.PasswordResetView.as_view(template_name="password_reset.html") , name="password_reset") , 
# パスワードリセット(メール送信完了)
    path("password_reset/done/" , auth_view.PasswordResetDoneView.as_view(template_name="password_reset_sent.html") , name="password_reset_done") , 
# リセットページ
    path("reset/<uidb64>/<token>" , auth_view.PasswordResetConfirmView.as_view(template_name="password_reset_form.html") ,  name="password_reset_confirm"),
# リセット完了
path("reset/done/" , auth_view.PasswordResetCompleteView.as_view(template_name="password_reset_done.html") ,  name="password_reset_complete")
]