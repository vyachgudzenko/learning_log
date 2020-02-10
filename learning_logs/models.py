from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """Модель данных тем обсуждения"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        """Возвращает текстовое представление модели"""
        return self.text

class Entry(models.Model):
    """Информация, изученная пользователем по теме"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name_plural = 'enrties'

    def __str__(self):
        return self.text[:50] + "..."
