from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('maps/', views.maps, name='maps'),
    path('profile/', views.profile, name='profile'),
    path('subscribe/', views.email_list_signup, name='subscribe'),
    path('calendar/', views.calendar, name='calendar'),

    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

]
