from django.contrib import admin
from .models import CustomUser
from django.contrib import admin

# カスタムユーザを使う場合の設定
class CustomUserAdmin(admin.ModelAdmin):
    # 表示の値
    list_display= ('id' , 'username')  
    
    # 表示するカラムにリンクを設定
    list_display_links = ('id' , 'username')
    
# モデルの登録
admin.site.register(CustomUser ,CustomUserAdmin) 