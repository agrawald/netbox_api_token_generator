
from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path(r'token', views.ApiLoginView.as_view(), name='token')
]