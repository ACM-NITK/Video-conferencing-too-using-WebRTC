from django.urls import path
from .views import *


urlpatterns = [
    path('meet/<str:room_id>/<str:user_name>/<str:randomKey>', home_page, name="home_page"),
    path('api/<str:room_id>/<str:user_name>/', MeetingUrl.as_view()),
]
