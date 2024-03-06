from django.urls import path
from rest_framework import routers
from .views import IslandView, IslandListView

app_name = "IslandApi"
router = routers.DefaultRouter()
router.register(r'island', IslandView, basename='student')

urlpatterns = [
    path('island-sort', IslandListView.as_view(), name='Island'),
]
urlpatterns += router.urls
