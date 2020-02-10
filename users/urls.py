from django.urls import path
from . import views
from django.contrib.auth import login
#импортируем с другим названием, что бы не пересекалось с основными представлениями
from django.contrib.auth import views as auth_views

app_name = 'users'
urlpatterns = [
    #создаем путь без создания представление, а используя импортированное
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('register/',views.register, name='register'),
]
