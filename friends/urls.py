
from django.urls import path, include
from .views import *

urlpatterns = [
    # 아무것도 없을 때 매칭
    # http://127.0.0.1/Friends/
    path('', FriendsListView.as_view(), name='list'),
    path('add/', FriendsCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', FriendsDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', FriendsUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', FriendsDeleteView.as_view(), name='delete'),
]

