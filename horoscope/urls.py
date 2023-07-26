from django.urls import path
from . import views
# Дополнительный конфиг url для расширения

urlpatterns = [
    path('<sign_zodiac>', views.get_info_about_sign_zodiac),
]