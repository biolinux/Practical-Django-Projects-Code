from django.shortcuts import render_to_response
from django.contrib.flatpages.models import FlatPage
from django.http import HttpResponseRedirect


def search(request):
    # If query then using get method of the dictionary, we will get that query(searched word)
    # If there is no query, then query will have the second parameter of the get i.e., '' which
    # is None

    query = request.GET.get('q','')
    keyword_results = results = []
    if query:
        keyword_results = FlatPage.objects.filter(searchkeyword__keyword__in=query.split()).distinct()
        # If the result is single, then we can add this simple feature.
        # We will directly redirect the user to the target page.
        if keyword_results.count() == 1:
            return HttpResponseRedirect(keyword_results[0].get_absolute_url())
        results = FlatPage.objects.filter(content__icontains=query)
    return render_to_response('search/search.html',{'query':query,
                                                    'keyword_results': keyword_results,
                                                    'results':results})
