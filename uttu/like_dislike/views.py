from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.


from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import View
from .forms import CommentForm
from stackoverflow.models import Comment,DisLike,Like


class Requirement(View):
    form_class = CommentForm
    template_name = 'uttu_1/like_dislike.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        comment = Comment.objects.all()

        context = {}
        context['page_obj'] = comment
        context['form'] = form

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            comment_form = form.save(commit=False)
            comment_form.user = request.user
            comment_form.save()
            messages.success(request, 'Your comment successfully addedd')

            return HttpResponseRedirect(reverse('comment'))

        context = {}
        context['form'] = form

        return render(request, self.template_name, context)


class UpdateCommentVote(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self, request, *args, **kwargs):

        comment_id = self.kwargs.get('comment_id', None)
        option = self.kwargs.get('option', None)  # like or dislike button clicked

        comment = get_object_or_404(Comment, id=comment_id)

        try:
            # If child DisLike model doesnot exit then create
            comment.dis_likes
        except Comment.dis_likes.RelatedObjectDoesNotExist as identifier:
            DisLike.objects.create(comment=comment)

        try:
            # If child Like model doesnot exit then create
            comment.likes
        except Comment.likes.RelatedObjectDoesNotExist as identifier:
            Like.objects.create(comment=comment)

        if option.lower() == 'like':

            if request.user in comment.likes.users.all():
                comment.likes.users.remove(request.user)
            else:
                comment.likes.users.add(request.user)
                comment.dis_likes.users.remove(request.user)

        elif option.lower() == 'dis_like':

            if request.user in comment.dis_likes.users.all():
                comment.dis_likes.users.remove(request.user)
            else:
                comment.dis_likes.users.add(request.user)
                comment.likes.users.remove(request.user)
        else:
            return HttpResponseRedirect(reverse('comment'))
        return HttpResponseRedirect(reverse('comment'))