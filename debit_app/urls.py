from django.urls import path

from . import views
from .views import UserView, UserDetailView

urlpatterns = [
    path('', views.endpoints),
    path('user/', UserView.as_view()),
    path('user/<int:id>', UserDetailView.as_view()),
]
