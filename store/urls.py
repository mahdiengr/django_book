from django.urls import path, include
from . import views
urlpatterns = [
    path('add_book/', views.add_book, name='add_book'),
    path('show_book/', views.show_book, name='show_book'),
    path('edit_book/<int:id>', views.edit_book, name='edit_book'),
    path('delete_book/<int:id>', views.delete_book, name='delete_book'),
    path('search/', views.item_list, name='item_list'),
    path('no_search/', views.no_search_value, name='no_search'),
    
    
    
    
]