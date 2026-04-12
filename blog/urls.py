from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home),
    
    path('delete/<int:id>/', views.delete_post, name='delete_post'),
    path('edit/<int:id>/', views.edit_post, name='edit_post'),

    path('create/', views.create_post, name='create_post'),

    # Signup
    path('signup/', views.signup, name='signup'),

    # Login
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    # Logout
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]




