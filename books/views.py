# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Import Q object for book search
from django.db.models import Q

# Import for pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Import the models
from .models import Books


# View all objects
def fetch_all(request):

    obj = Books.objects.all()
    paginator = Paginator(obj, 12)

    page = request.GET.get('page')
    try:
        page = paginator.page(page)
    except PageNotAnInteger:
         # If page not an int deliver 1st page
         page = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver the first page
         page = paginator.page(paginator.num_pages)

    context = {'title': 'All Books','pages':page}
    return render(request, 'books/index.html', context)


# View for single objects
def fetch_single(request,title, type):

    obj = Books.objects.get(title=title, type=type)
    context = {'object': obj,'type': type, 'title':title}
    return render(request, 'books/details.html', context)

# View for objects in categories
def fetch_category(request, type):

    obj = Books.objects.filter(type__exact=type)
    paginator = Paginator(obj, 12)
    page = request.GET.get('page')

    try:
        page = paginator.page(page)
    except PageNotAnInteger:
         # If page not an int deliver 1st page
         page = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver the first page
         page = paginator.page(paginator.num_pages)

    context = {'pages':page, 'title': type}
    return render(request, 'books/categories.html', context)


def search(request):

    template = 'books/search.html'
    query = request.GET.get('q')
    if query:
        results = Books.objects.filter(
            Q(title__icontains=query) | Q(type__icontains=query) | Q(author__icontains=query)
        )
    else:
        results = Books.objects.all()


    # Pagination
    paginator = Paginator(results, 12)
    page = request.GET.get('page')

    try:
        page = paginator.page(page)
    except PageNotAnInteger:
         # If page not an int deliver 1st page
         page = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver the last page
         page = paginator.page(paginator.num_pages)

    context = {'pages': page, 'query':query}

    return render(request, template, context)
