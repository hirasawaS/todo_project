# Generated by Django 3.1 on 2023-08-26 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_middletask_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bottomtask',
            name='status',
            field=models.BooleanField(default=False, verbose_name='完了フラグ'),
        ),
    ]
