from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    """Завершает сеанс работы с приложением"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    """Регистрируем нового пользователя"""
    if request.method != 'POST':
        #Создание пустой формы
        form = UserCreationForm()
    else:
        #Обработка заполненной формы
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            #Выполнение входа и перенаправление на домашнюю страницу
            authenticated_user = authenticate(username=new_user.username,
                                 password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form':form}
    return render(request, 'users/register.html',context)                             