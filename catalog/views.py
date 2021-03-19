from django.shortcuts import render
from .models import Book, BookInstance, Language, Author, Genre

# Create your views here.


def index(request):
    """
    Функция отображения для домашней страницы сайта
    :param request:
    :return:
    """
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    num_languages = Language.objects.count()
    num_genres = Genre.objects.count()
    num_books_contains = Book.objects.filter(title__icontains='Чист').count()

    # Отрисовка HTML-шаблона index.html
    return render(
        request,
        'index.html',
        context={
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
            'num_languages': num_languages,
            'num_genres': num_genres,
            'num_books_contains': num_books_contains
        }
    )
