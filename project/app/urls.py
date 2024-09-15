from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import DashboardView


urlpatterns = [
    path('', views.index, name='index'),
    path('student/', views.student_dashboard, name='student_dashboard'),
    path('login/', views.user_login, name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('user_management/', views.user_management, name='user_management'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('update_user/<int:user_id>/', views.update_user, name='update_user'),
    path('form_templates/', views.form_template_view, name='form_templates'),
    path('notifications/', views.notification_view, name='notifications'),
    path('home/', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('data_management/', views.data_management_view, name='data_management'),
    path('', views.list_excel_files, name='list_excel_files'),
    path('download/<int:pk>/', views.download_excel_file, name='download_excel_file'),
    path('settings/', views.settings_view, name='settings'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
