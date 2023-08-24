from django.urls import path

from . import views
from .views import UserView, UserDetailView, AccountView, AccountDetailView, CardView, CardDetailView, TransactionView

urlpatterns = [
    path('', views.endpoints),
    path('user/', UserView.as_view()),
    path('user/<int:id>', UserDetailView.as_view()),
    path('account/', AccountView.as_view()),
    path('account/<int:id>', AccountDetailView.as_view()),
    path('card/', CardView.as_view()),
    path('card/<int:id>', CardDetailView.as_view()),
    path('transaction/', TransactionView.as_view()),
]
