from django.shortcuts import render
from .models import Journal,Author,Category
# Create your views here.
from django.db.models import Q

def BootstrapFilterView(request):
    empty_string = ''
    which_query=''
    qs = Journal.objects.all()
    title_contains_query = request.GET.get('title_contains')
    id_exact_query = request.GET.get('id_exact')
    title_or_author_query = request.GET.get('title_or_author')


    if title_contains_query != empty_string and title_contains_query is not None:
        qs = qs.filter(title__icontains=title_contains_query)

        which_query+=title_contains_query

        ''' {1}_icontains IS METHOD TO SEARCH {1} FIELD IN "Journal" MODEL'''


    elif id_exact_query != empty_string and id_exact_query is not None:
        qs = qs.filter(id=id_exact_query)

        which_query+=id_exact_query


    elif title_or_author_query != empty_string and title_or_author_query is not None:

        # Q IS USED FOR SEARCHING IN MORE THEN ONE MODEL FIELDS
        qs = qs.filter(Q(title__icontains=title_or_author_query) | Q(author__name__icontains=title_or_author_query)).distinct()

        which_query+=title_or_author_query


        ''' ".distinct" is used if query is found in both of the filter then it will return only one query'''

        ''' {1}_{2}_icontains IS METHOD TO SEARCH {2} FIELD FROM MODEL {1} WHICH IS ASSOCIATED WITH "Journal" MODAL '''


    context = {
        'queryset': qs,
        'which_query':which_query
    }

    return render(request, "djfilter/bootstrap_form.html", context)