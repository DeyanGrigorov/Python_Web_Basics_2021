from django.shortcuts import render
from django.http import HttpResponse
from python_web_basics_2021.cities.models import Person


def index(req):
    context = {
        'name': 'Deyan',
        'people': Person.objects.all(),

    }
    return render(req, 'index.html', context)


def list_phones(req):
    context = {
        'phones': [
            'Galaxy s20',
            'Xiaomi MI11 light',
            'Huawei Mate20 Pro',
        ]
    }
    return render(req, 'phones.html', context)

