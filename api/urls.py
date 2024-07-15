from django.urls import path
from .views import SendMessage, GetMessage

urlpatterns = [
    path('send-message', SendMessage.as_view()),
    path('get-message', GetMessage.as_view())
]