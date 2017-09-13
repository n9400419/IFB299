from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

from .models import College, Library, Industry, Hotel, Park, Zoo, Museum, Restaurant, Mall

type_list = {'park':Park,
             'library':Library,
             'college':College,
             'industry':Industry,
             'hotel':Hotel,
             'zoo':Zoo,
             'museum':Museum,
             'restaurant':Restaurant,
             'mall':Mall
}


def search(request):
    return render(request, 'search/search.html')

def results(request):
    query = request.GET['query']
    search_type = request.GET['search_type']

    print(query)
    print(search_type)
    results = type_list[search_type].objects.raw("SELECT id, name FROM search_" +
                                                 search_type + " WHERE name LIKE '%%" +
                                                 query + "%%'")
    #results = 0

    
    context = { 'results' : results }
    return render(request, 'search/results.html', context)
