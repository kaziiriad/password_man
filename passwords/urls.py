from django.urls import path
from . import views


app_name = 'passwords'
urlpatterns = [
    path(
        '', 
        views.password_url_list, 
        name='password-url-list'
    ),

    path(
        'password-url/<int:pk>/', 
        views.password_url_detail, 
        name='password-url-detail'
    ),

    path(
        'password-url/<int:pk>/password-entry/create/', 
        views.password_entry_create, 
        name='password-entry-create'
    ),
    
    path(
        'password-entry/<int:pk>/update/', 
        views.password_entry_update, 
        name='password-entry-update'
    ),

    path(
        'password-entry/<int:pk>/delete/', 
        views.password_entry_delete, 
        name='password-entry-delete'
    ),

    path(
        'accounts/login/',
        views.login_view,
        name='login'
    ),
]
