# Generated by Django 3.1 on 2023-08-21 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(choices=[(1, 'top'), (2, 'middle'), (3, 'bottom')], verbose_name='カテゴリのレベル')),
                ('category', models.CharField(max_length=20, verbose_name='カテゴリ名')),
            ],
        ),
        migrations.CreateModel(
            name='TopTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='タイトル')),
                ('description', models.TextField(verbose_name='説明')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='todoapp.category', verbose_name='カテゴリ')),
            ],
        ),
        migrations.CreateModel(
            name='MiddleTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='タイトル')),
                ('description', models.TextField(verbose_name='説明')),
                ('status', models.IntegerField(verbose_name='進捗率')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='todoapp.category', verbose_name='カテゴリ')),
                ('incharge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='担当者')),
                ('parent_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todoapp.toptask', verbose_name='親タスク')),
            ],
        ),
        migrations.CreateModel(
            name='BottomTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='タイトル')),
                ('description', models.TextField(verbose_name='説明')),
                ('status', models.IntegerField(choices=[(0, '未着手'), (30, '着手中'), (60, '後半'), (90, '確認のみ'), (100, '完了')], verbose_name='進捗率')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='todoapp.category', verbose_name='カテゴリ')),
                ('parent_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todoapp.middletask', verbose_name='親タスク')),
            ],
        ),
    ]
