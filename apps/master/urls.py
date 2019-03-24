from django.urls import path

from .views import Logs

app_name = 'master'
urlpatterns = [
    path('logs/', Logs.as_view(), name='logs')
]
