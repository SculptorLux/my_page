from django.urls import path
from . import views
# Дополнительный конфиг url для расширения

urlpatterns = [
    path('leo/', views.leo),
    path('scorpio/', views.scorpio),
]