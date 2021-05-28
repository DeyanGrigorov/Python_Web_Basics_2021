from django.urls import path

from python_web_basics_2021.cities.views import index, list_phones

urlpatterns = [
    path('', index),
    path('phones/', list_phones)
]
