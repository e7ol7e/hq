from django.urls import path
from .views import ListAllLessonsView, ListUserLessonsView, ProductStatisticsView

urlpatterns = [
    path('all-lessons/', ListAllLessonsView.as_view(), name='all-lessons'),
    path('user-lessons/', ListUserLessonsView.as_view(), name='user-lessons'),
    path('product-statistics/', ProductStatisticsView.as_view(), name='product-statistics'),
]
