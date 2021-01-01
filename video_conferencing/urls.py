from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('meet/<str:room_id>/<str:user_name>/', home_page, name="home_page"),
    path('api/<str:room_id>/<str:user_name>/', APIResponse.as_view()),
]
