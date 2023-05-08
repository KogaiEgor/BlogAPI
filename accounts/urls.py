from django.urls import path
from .views import signup, login

urlpatterns = [
    path('signup/', signup.as_view()),
    path('login/', login.as_view())
]