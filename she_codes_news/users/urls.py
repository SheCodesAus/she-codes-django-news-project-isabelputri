from django.urls import path
from . import views
from .views import CreateAccountView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('profile/<int:pk>/', views.UserProfileView.as_view(), name='profile'),
]
