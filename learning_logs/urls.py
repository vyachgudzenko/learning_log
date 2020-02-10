from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    #Вывод домашней страницы
    path('', views.index, name='index'),
    #Вывод всех тем
    path('topics/',views.topics, name='topics'),
    #Страница с информацией по выбранной теме
    #path('^topics/(?P<topic_id>\d+)', views.topic, name='topic'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #Страница для создания новой темы
    path('new_topic/',views.new_topic, name='new_topic'),
    #Страница для добавления новой информации
    path('topics/<int:topic_id>/new_entry/', views.new_entry, name='new_entry'),
    #Страница для редактирования записи
    path('topics/edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
