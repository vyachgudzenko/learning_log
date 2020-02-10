from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """Класс для создания формы для темы"""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}

class EntryForm(forms.ModelForm):
    """Класс для создания формы для информации"""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widgets = {'text':forms.Textarea(attrs={'cols':80})}
