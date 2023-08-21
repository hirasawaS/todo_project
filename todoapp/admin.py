from django.contrib import admin
from .models import Category , TopTask , MiddleTask , BottomTask 
from accounts.models import CustomUser


class CategoryAdmin(admin.ModelAdmin):
    
    class Meta:
        list_display = ("id" , "title")
        list_display_links = ("id" , "title")
        
class TopTaskAdmin(admin.ModelAdmin):
    
    class Meta:
        list_display = ("id" , "title")
        list_display_links = ("id" , "title")
        
class MiddleTaskAdmin(admin.ModelAdmin):
    
    class Meta:
        list_display = ("id" , "title")
        list_display_links = ("id" , "title")
        

class BottomTaskAdmin(admin.ModelAdmin):
    
    class Meta:
        list_display = ("id" , "title")
        list_display_links = ("id" , "title")
        

admin.site.register(Category , CategoryAdmin)
admin.site.register(TopTask , TopTaskAdmin)
admin.site.register(MiddleTask , MiddleTaskAdmin)
admin.site.register(BottomTask , BottomTaskAdmin)