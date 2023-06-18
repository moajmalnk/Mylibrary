from django.shortcuts import render
from mylibrary.models import *
from django.db.models import Q


def search_result(request):
    books = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        books = Book_details.objects.all().filter(
            Q(name__contains=query) |
            Q(slug__contains=query) |
            Q(desc__contains=query) |
            Q(auther__contains=query) |
            Q(price__contains=query)
        )
    context = {
        'query': query,
        'books': books
    }
    return render(request, 'search.html', context)


def patrons(request):
    patron = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        patron = Patron.objects.all().filter(
            Q(name__contains=query) |
            Q(gmail__contains=query) |
            Q(card_no__contains=query) |
            Q(phone__contains=query)
        )
    context = {
        'query': query,
        'books': patron
    }
    return render(request, 'patron_search.html', context)