from django.shortcuts import render
from .models import BottomTask
from django import forms

class ButtomTaskForm(forms.ModelForm):    
    class Meta:
        model = BottomTask
        fields= ("title" ,"parent_task" , "description" ,"category")

    def __init__(self , *args ,**kwargs):
        super().__init__(*args , **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
        