from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404
from .models import Topic,Entry
from .forms import TopicForm,EntryForm
#Импортируем декоратор для ограничения просмотра некоторых страниц
from django.contrib.auth.decorators import login_required

def index(request):
    """Домашняя страница проекта"""
    return render(request, 'learning_logs/index.html')

#Добавляем декоратор для конкретных представлений
@login_required
def topics(request):
    """Вывод всех тем"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics':topics}
    return render(request,'learning_logs/topics.html',context)

@login_required
def topic(request,topic_id):
    """Выводит одну тему и все ее записи"""
    topic = Topic.objects.get(id=topic_id)
    #Проверка того, что тема принадлежит текущему пользователю
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request,'learning_logs/topic.html',context)

@login_required
def new_topic(request):
    """Определяет новую тему"""
    if request.method != 'POST':
        #Данные не отправлялись, создается новая форма
        form = TopicForm()
    else:
        #отправленны данные, обработать данные
        form =TopicForm(request.POST)
        #если форма проходит валидацию
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form':form}
    return render(request,'learning_logs/new_topic.html',context)

@login_required
def new_entry(request, topic_id):
    """Добавляет новую запись по конкретной теме"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id]))
    context = {'topic':topic,'form':form}
    return render(request,'learning_logs/new_entry.html',context)

@login_required
def edit_entry(request,entry_id):
    """Редактирует существующую запись"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        #Форма заполняется текущими данными
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))
    context = {'entry':entry,'topic':topic,'form':form}
    return render(request,'learning_logs/edit_entry.html', context)