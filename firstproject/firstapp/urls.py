from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('seed-menu/', views.seed_menu, name='seed_menu'),
    path('function', views.hello),
    path('class', views.HelloWorld.as_view()),
]