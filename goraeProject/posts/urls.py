from rest_framework.routers import SimpleRouter, DefaultRouter
from django.urls import path, include
from .views import MessageViewSet



message_router = DefaultRouter(trailing_slash=True)
message_router.register('messages', MessageViewSet, basename='message')

urlpatterns = [
    path('', include(message_router.urls)),
]