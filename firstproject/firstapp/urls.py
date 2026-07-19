from django.urls import path
from . import views


urlpatterns = [  # Fix: was 'urlpattern' (missing 's'), Django requires exactly 'urlpatterns'
    path('function', views.hello),
    path('class', views.HelloWorld.as_view()),
]