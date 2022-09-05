from django.urls import path
from . import views

urlpatterns = [
    path('', views.accountsView, name='home'),
    path('create', views.accountsCreate, name='create'),
    path('update/<str:pk>/', views.accountsUpdate, name='update'),
    path('delete/<int:pk>/', views.accountsDelete, name='delete'),
    path('users/register', views.register, name='register'),
    path('users/login', views.login_user, name='login'),
    path('users/logout', views.logout_user, name='logout'),
    path('search', views.search, name='search'),
    
]
