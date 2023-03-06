from django.urls import path

from .views import GetPostAPIView

app_name = 'social'

urlpatterns = [
    path('get-posts/', GetPostAPIView.as_view(), name='get-posts'),

]
