from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import get_template
from xhtml2pdf import pisa

from .forms import ImageForm, PostForm
from .models import postPdfTesting, Images

from django.views.generic import ListView
from uttu_1.models import MyModel

from uttu_1.tables import MyTable

# Create your views here.



class PostPdfListView(ListView):
     model = postPdfTesting
     template_name = 'uttu_1/pdf_main.html'
     context_object_name = 'object_list'


def user_pdf_render_view(request):
    template_path = 'uttu_1/tablesPdf.html'
    context = {'myvar': 'mit sdjf dbsvd sndvuyg'}

    #context_object_name='object_list'


    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # to Download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # to Display
    response['Content-Disposition'] = 'filename="report.pdf"'


    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)

    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
    pass


def render_pdf_view(request):
    context_=postPdfTesting.objects.all()
    #context_=MyModel.objects.all()


    template_path = 'uttu_1/pdf_main.html'
    context = {'object_list': context_}


    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # to Download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # to Display
    response['Content-Disposition'] = 'filename="report.pdf"'


    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)

    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



@login_required
def post(request):
    ImageFormSet = modelformset_factory(Images,form=ImageForm, extra=3)

    if request.method == 'POST':
        postForm = PostForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,queryset=Images.objects.none())

        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.user = request.user
            post_form.save()

            for form in formset.cleaned_data:
                image = form['image']
                photo = Images(post=post_form, image=image)
                photo.save()
            messages.success(request,"Posted!")
            return HttpResponseRedirect("/")
        else:

            messages.warning(postForm.errors,formset.errors)

    else:

        postForm = PostForm()
        formset = ImageFormSet(queryset=Images.objects.none())
        context={
                'postForm': postForm,
                 'formset': formset
                }

        return render(request, 'uttu_1/muf.html',context)



