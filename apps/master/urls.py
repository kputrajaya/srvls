from django.urls import path

from .views import Logs, Ping

app_name = 'master'
urlpatterns = [
    path('ping/', Ping.as_view(), name='ping'),
    path('logs/', Logs.as_view(), name='logs')
]
