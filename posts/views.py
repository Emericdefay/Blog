from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from posts.forms import PostCreateForm
from posts.models import Post, Tag

from typing import cast
import os
from django.contrib.auth.models import User

class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    if os.getenv('NEED_ACCT', 'False').lower() in ('True', '1', 'true'):
        User.objects.create_superuser(
            username=cast(str, os.getenv('USER_ADMIN')),
            email=cast(str, os.getenv('EMAIL_ADMIN')),
            password=cast(str, os.getenv('PASSW_ADMIN'))
            )


class PostDetailView(DetailView):
    model = Post
    template_object_name = 'post'
    template_name = 'posts/post_detail.html'


class CreateUpdateMixin(LoginRequiredMixin, UserPassesTestMixin,
                        SuccessMessageMixin):
    def form_valid(self, form):
        action = self.request.POST.get('action')
        if action == 'SAVE':
            print(self.request.POST)
            return super().form_valid(form)
        elif action == 'PREVIEW':
            preview = Post(
                title=form.cleaned_data['title'],
                excerpt=form.cleaned_data['excerpt'],
                content=form.cleaned_data['content'],
            )
            context = self.get_context_data(preview=preview)
            return render(self.request, 'posts/post_preview.html', context)

    def test_func(self):
        if self.request.user.is_authenticated and self.request.user.is_staff:
            return True
        return False


class PostCreateView(CreateUpdateMixin, CreateView):
    form_class = PostCreateForm
    template_name = 'posts/post_form.html'
    success_message = 'Post created successful'
    extra_context = {
        'title': 'Create Post'
    }


class PostUpdateView(CreateUpdateMixin, UpdateView):
    model = Post
    form_class = PostCreateForm
    success_message = 'Post updated successful.'
    extra_context = {
        'title': 'Update Post'
    }


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,
                     SuccessMessageMixin, DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = '/'
    success_message = 'Post deleted successful.'

    def test_func(self):
        if self.request.user.is_authenticated and self.request.user.is_staff:
            return True
        return False


class TagDetailView(DetailView):
    model = Tag
    template_name = 'posts/post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = Tag.objects.get(slug=self.kwargs['slug'])
        context['object_list'] = tag.post_set.all()
        return context
