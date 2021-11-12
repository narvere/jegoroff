from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:sign_zodiac>', views.show_sign_zodiac_by_nr),
    path('<str:sign_zodiac>', views.show_sign_zodiac, name='horoscope_name'),

]
