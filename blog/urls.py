from django.urls import path
from .views import BlogViews, CreateRecord

urlpatterns = [
    path('blogs/', BlogViews.as_view()),
    path('createrecord/', CreateRecord.as_view())
]