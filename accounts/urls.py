from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('',views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('info/<str:username>/', views.info, name='info'),
    path('follow/<str:username>/', views.follow, name='follow'),
    ]