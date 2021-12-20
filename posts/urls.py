from django.urls import path
from .views import PosteList,PosteDetial

urlpatterns = [
    path('',PosteList.as_view(),name='post_list'),
    path('<int:pk>/',PosteDetial.as_view(),name='post_detail'),
]