from django.urls import path
from . import views

app_name = 'passwords'
urlpatterns = [
    path(
        '', 
        views.password_url_list, 
        name='password_url_list'
    ),

    path(
        'password-url/<int:pk>/', 
        views.password_url_detail, 
        name='password_url_detail'
    ),

    path(
        'password-url/<int:pk>/password-entry/create/', 
        views.password_entry_create, 
        name='password_entry_create'
    ),
    
    path(
        'password-entry/<int:pk>/update/', 
        views.password_entry_update, 
        name='password_entry_update'
    ),

    path(
        'password-entry/<int:pk>/delete/', 
        views.password_entry_delete, 
        name='password_entry_delete'
    ),
]
