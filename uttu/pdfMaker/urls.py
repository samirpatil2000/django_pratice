
from django.urls import path
from django import views
from . import views
from .views import PostPdfListView
#
urlpatterns = [
    path('test/',views.render_pdf_view,name='pdfHomeTest'),
    path('',PostPdfListView.as_view(),name='pdfHome'),
    path('userPdf/',views.user_pdf_render_view,name='pdfHome'),

 ]