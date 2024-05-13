from datetime import datetime
from random import choice

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseNotFound
from books.models import BOOKS


def current_time(request: HttpRequest) -> HttpResponse:
    now = datetime.now()
    return HttpResponse(now)


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Добро пожаловать</h1>")


def random_book(request: HttpRequest) -> HttpResponse:
    return JsonResponse(
        choice(BOOKS),

        json_dumps_params={
            "indent": 4,
            "ensure_ascii": False
        }
    )


def view_all_book(request):
    return JsonResponse(
        BOOKS,
        safe=False,
        json_dumps_params={
            "indent": 4,
            "ensure_ascii": False
        }
    )




def custom_404(request: HttpRequest, exception) -> HttpResponse:
    return HttpResponse('упс 404', status=404)
