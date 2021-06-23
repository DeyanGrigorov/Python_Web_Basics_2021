from django.urls import path

from python_web_basics_2021.cities.views import index, list_phones, create_person, show_forms_demo

urlpatterns = [
    path('', index),
    path('phones/', list_phones),
    path('create/', create_person),
    path('forms/', show_forms_demo)
]
