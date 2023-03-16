from django.urls import path
from . import views


urlpatterns = [

    path(
        'password_url/create/',
        views.password_url_create,
        name='password_url_create'
    ),

    path(
        '', 
        views.password_url_list, 
        name='password_url_list'
    ),

    path(
        'password_url/<int:pk>/', 
        views.password_url_detail, 
        name='password_url_detail'
    ),

    path(
        'password_url/<int:pk>/password-entry/create/', 
        views.password_entry_create, 
        name='password_entry_create'
    ),
    
    path(
        'password_entry/<int:pk>/update/', 
        views.password_entry_update, 
        name='password_entry_update'
    ),

    path(
        'password_entry/<int:pk>/delete/', 
        views.password_entry_delete, 
        name='password_entry_delete'
    ),

    path(
        'accounts/login/',
        views.login_view,
        name='login'
    ),
]
