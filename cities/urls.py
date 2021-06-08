from django.urls import path

from python_web_basics_2021.cities.views import index, list_phones, create_person

urlpatterns = [
    path('', index),
    path('phones/', list_phones),
    path('create/', create_person),

]
