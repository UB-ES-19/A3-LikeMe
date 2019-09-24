from django.urls import path, url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
        path('', views.index, name='index'),
        path('register/', views.register, name='register'),
        url(r'^accounts/login/$', login, name='login'),
        url(r'^accounts/logout/$', logout, {'next_page': '/'}, name='logout')
    ]
