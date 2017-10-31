from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

from .models import College, Library, Industry, Hotel, Zoo, Museum, Restaurant, Mall, Park

type_list = {'park': Park,
             'library': Library,
             'college': College,
             'industry': Industry,
             'hotel': Hotel,
             'zoo': Zoo,
             'museum': Museum,
             'restaurant': Restaurant,
             'mall': Mall
             }


def results(request):
    query = request.GET['query']
    search_type = request.GET['search_type']

    results = type_list[search_type].get_city_objects(search_type, type_list[search_type], query)

    context = {'results': results}
    return render(request, 'results.html', context)


