
from . import views
from django.urls import path, include
import products

urlpatterns = [
    path('signup/', views.signup, name = 'signup'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('login_page/', views.login_page, name = 'login_page'),
    path('login/products/1/', views.PD, name = 'linked_page'),
]
