from django.urls import path
from . import views

urlpatterns = [
    #add following lines to urlpatterns list 
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]
