from datetime import datetime
from random import choice

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse, Http404
from books.models import BOOKS, CATEGORIES


def custom_404(request: HttpRequest, exception) -> HttpResponse:
    return HttpResponse('упс 404', status=404)


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
    query_param = request.GET
    query_published = query_param.get('published_year')

    books = BOOKS.copy()
    if query_published is not None:
        query_published = int(query_published)
        books = [book
                 for book in books
                 if book['published_year'] == query_published
                 ]
    return JsonResponse(
        books,
        safe=False,
        json_dumps_params={
            "indent": 4,
            "ensure_ascii": False
        }
    )


def get_categories(request: HttpRequest) -> HttpResponse:
    return JsonResponse(
        CATEGORIES,
        safe=False,
        json_dumps_params={
            "indent": 4,
            "ensure_ascii": False
        }
    )


def get_one_book(request: HttpRequest, book_id: int) -> HttpResponse:
    for book in BOOKS:
        if book['id'] == book_id:
            return JsonResponse(
                book,
                json_dumps_params={
                    'indent': 4,
                    'ensure_ascii': False
                }
            )
    raise Http404('Не верный id')


def get_book_by_category(request: HttpRequest, category_slug: str) -> HttpResponse:

    return JsonResponse(
        [book for book in BOOKS if book["category"] == category_slug],
        safe=False,
        json_dumps_params={
            "indent": 4,
            "ensure_ascii": False
        }
    )
