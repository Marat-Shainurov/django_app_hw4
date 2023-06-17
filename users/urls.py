from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, verify_email, restore_user, login_warning

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register/verification/<str:email>', verify_email, name='verify_email'),
    path('login/restore/', restore_user, name='restore_user'),
    path('login/login_warning/', login_warning, name='login_warning')
]
