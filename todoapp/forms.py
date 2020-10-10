from django import forms
from .models import TodoListItem


class TodoListItemForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new item...'}))
    class Meta:
        model = TodoListItem
        fields = '__all__'
