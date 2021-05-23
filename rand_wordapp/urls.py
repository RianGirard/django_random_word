from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),                  # localhost:8000 aka, the root route
    path('random_word', views.random),      # localhost:8000/random_word
    path('reset', views.reset),             # localhost:8000/reset
]