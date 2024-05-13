from django.contrib import admin
from django.urls import path, include
from books import views

handler404 = "books.views.custom_404"


urlpatterns = [
    path("", views.index),
    path('admin/', admin.site.urls),
    path("current-time/", views.current_time),
    path("books/random-book", views.random_book),
    path("books/", views.view_all_book),
    path("books/<int:book_id>", views.get_one_book),
    path("books/categories", views.get_categories),
    path("books/categories/<slug:category_slug>", views.get_book_by_category)
]
