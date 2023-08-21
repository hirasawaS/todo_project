from django.db import models
from accounts.models import CustomUser


STATUS  = ((0 , "未着手") ,
        (30 , "着手中") ,
        (60 ,"後半") , 
        (90 , "確認のみ") , 
        (100 , "完了"))

LEVEL = ((1 ,"top") , 
        (2 ,"middle" ) , 
        (3 , "bottom"))


class Category(models.Model):
    level =models.IntegerField(
        verbose_name="カテゴリのレベル" , 
        choices=LEVEL)
    
    category = models.CharField(
        verbose_name="カテゴリ名" ,
        max_length=20
        
    )

class TopTask(models.Model):
    title = models.CharField(
        verbose_name="タイトル" ,
        max_length=30 , 
    ) 
    
    description = models.TextField(
        verbose_name="説明"
    )
    
    category = models.ForeignKey(
        Category ,
        verbose_name="カテゴリ" , 
        on_delete=models.PROTECT
    )


class MiddleTask(models.Model):
    title = models.CharField(
        verbose_name="タイトル" ,
        max_length=30 , 
    ) 
    
    description = models.TextField(
        verbose_name="説明"
    )
    
    category = models.ForeignKey(
        Category ,
        verbose_name="カテゴリ" , 
        on_delete=models.PROTECT
    )
    
    parent_task = models.ForeignKey(
        TopTask , 
        verbose_name="親タスク" , 
        on_delete=models.CASCADE
    )
    
    incharge = models.ForeignKey(
        CustomUser , 
        verbose_name="担当者" , 
        on_delete=models.CASCADE
    ) 
    status = models.IntegerField(
        verbose_name="進捗率"   
    )

class BottomTask(models.Model):
    title = models.CharField(
        verbose_name="タイトル" ,
        max_length=30 , 
    ) 
    
    description = models.TextField(
        verbose_name="説明"
    )
    
    category = models.ForeignKey(
        Category ,
        verbose_name="カテゴリ" , 
        on_delete=models.PROTECT
    )
    
    parent_task = models.ForeignKey(
        MiddleTask , 
        verbose_name="親タスク" , 
        on_delete=models.CASCADE
    )
    
    status = models.IntegerField(
        verbose_name="進捗率"   , 
        choices=STATUS
    )
