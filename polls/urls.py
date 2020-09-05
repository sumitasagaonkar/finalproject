from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('constact', views.constact, name='constact'), 


    path('constactus/', views.constactPage, name='constactus'), 
    path('orderbook/', views.OrderbookPage, name='orderbook'), 
    path('askq/', views.askquaPage, name='askq'), 
    path('profile', views.profilePage, name='profile'),  
    path('setting', views.settingsPage, name='setting'),
    path('profilesetting', views.profilesettingPage, name='profilesetting'),
    path('accounts/logout/', views.logoutUser , name="logout"),

]