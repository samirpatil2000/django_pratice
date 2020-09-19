
from django.urls import path
from . import views
#
urlpatterns = [
    path('',views.BootstrapFilterView,name='song_home'),

 ]