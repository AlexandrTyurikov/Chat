from django.urls import path

from .views import RoomApi, DialogApi


urlpatterns = [
    path('room/', RoomApi.as_view()),
    path('dialog/', DialogApi.as_view()),
]
