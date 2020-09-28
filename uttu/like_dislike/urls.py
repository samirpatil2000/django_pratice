
from django.urls import path
from django import views
from .views import Requirement,UpdateCommentVote
urlpatterns = [

path('comments', Requirement.as_view(), name='requirements'),
path('requirement/<int:pk>/<str:option>', UpdateCommentVote.as_view(), name='requirement_comment_vote'),


 ]