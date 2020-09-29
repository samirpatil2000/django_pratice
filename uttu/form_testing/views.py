from django.shortcuts import render, redirect
from .forms import TestFrom
from .models import FormTesting
# Create your views here.

def createFormTest(request):
    form = TestFrom(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            post_item = form.save(commit=False)
            post_item.save()
            return redirect('/')
        else:
            return render(request, 'uttu_1/form_testing.html', {'form': form})
    else:
        form=TestFrom()

    return render(request, 'uttu_1/form_testing.html', {'form': form})
