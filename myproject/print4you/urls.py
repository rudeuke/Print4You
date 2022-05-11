from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('index/', views.index, name='index'),
    #path('accounts/', include('django.contrib.auth.urls')),
    #path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='myproject/register/templates/password/password_reset_complete.html'), name='password_reset_done'),
    #path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="myproject/register/templates/password/password_reset_confirm.html"), name='password_reset_confirm'),
    #path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='myproject/register/templates/password/password_reset_complete.html'), name='password_reset_complete'),
]
