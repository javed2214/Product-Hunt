
from . import views
from django.urls import path, include

urlpatterns = [
   path('create/', views.create, name = 'create'),
   path('<int:product_id>', views.detail, name = 'detail'),
   path('<int:product_id>/upvote', views.upvote, name = 'upvote'),
   path('myproducts/', views.myproducts, name = 'myproducts'),
]
