from django.shortcuts import render
from .models import Journal,Author,Category
# Create your views here.
from django.db.models import Q



empty_string = ''

def is_valid_params(param):
    return param!=empty_string and param is not None

def BootstrapFilterView(request):

    which_query=''
    between_date=''
    between_views=''

    qs = Journal.objects.all()
    title_contains_query = request.GET.get('title_contains')
    id_exact_query = request.GET.get('id_exact')
    title_or_author_query = request.GET.get('title_or_author')

    view_count_min = request.GET.get('view_count_min')
    view_count_max = request.GET.get('view_count_max')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')


    if is_valid_params( title_contains_query):
        qs = qs.filter(title__icontains=title_contains_query)

        which_query+=title_contains_query

        ''' {1}_icontains IS METHOD TO SEARCH {1} FIELD IN "Journal" MODEL'''


    elif is_valid_params(id_exact_query):

        qs = qs.filter(id=id_exact_query)
        which_query+=id_exact_query


    elif is_valid_params(title_or_author_query):

        # Q IS USED FOR SEARCHING IN MORE THEN ONE MODEL FIELDS
        qs = qs.filter(Q(title__icontains=title_or_author_query) | Q(author__name__icontains=title_or_author_query)).distinct()

        which_query+=title_or_author_query


        ''' ".distinct" is used if query is found in both of the filter then it will return only one query'''

        ''' {1}_{2}_icontains IS METHOD TO SEARCH {2} FIELD FROM MODEL {1} WHICH IS ASSOCIATED WITH "Journal" MODAL '''



    if is_valid_params(view_count_min):
         qs = qs.filter(views__gte=view_count_min)
         between_views+=str(view_count_min)

         ''' __gte ==> GREATER THAN EQUAL TO'''

    if is_valid_params(view_count_max):
         qs = qs.filter(views__lt=view_count_max)
         between_views+=str(view_count_max)


         ''' __ls ==> LESS THAN'''    # WE ARE NOT USING HERE ELSE STATEMENT BECAUSE WE CAN APPLY THEM TOGETHER ,
                                      # "view_count_min" , "view_count_max" , "date_min", "date_max"

    if is_valid_params(date_min):
         qs = qs.filter(publish_date__gte=date_min)

         between_date+=str(date_min)

    if is_valid_params(date_max):
         qs = qs.filter(publish_date__lt=date_max)

         between_date+=str(date_max)


    context = {
        'queryset': qs,
        'which_query':which_query,
        'between_dates':between_date,
        'between_views':between_views,
    }

    return render(request, "djfilter/bootstrap_form.html", context)