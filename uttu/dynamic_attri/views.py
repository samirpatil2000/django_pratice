from django.shortcuts import render
from .models import Item
# Create your views here.
def index(request):
    item=Item.objects.all()
    context={
        'obj':item,
    }
    return render(request,'dynamic_attri/dy-index.html',context)


from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Person, City
from .forms import PersonForm


class PersonListView(ListView):
    model = Person
    context_object_name = 'people'
    template_name = 'dynamic_attri/index.html'


class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('person_changelist')


class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('person_changelist')


def load_cities(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    context={
        'cities':cities,
    }
    return render(request, 'dynamic_attri/load_sub_cat.html',context)