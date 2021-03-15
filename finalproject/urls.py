
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from accounts.views import login_view, register_view, logout_view
from finalproject.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('accounts/login/', login_view, name="login"),
    path('accounts/register/', register_view, name="register"),
    path('accounts/logout/', logout_view, name="logout"),


    # reset password urls
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name = 'password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name = 'password_reset_complete'),
]
