from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Blog
from django.contrib.auth.mixins import LoginRequiredMixin


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ('header', 'text', 'preview',)
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.header)
            new_post.save()
        return super().form_valid(form)


class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = 'blog/blog_list.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ('header', 'slug', 'text', 'preview')

    def get_success_url(self):
        return reverse_lazy('blog:blog_details', args=[self.kwargs.get('pk')])

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.header)
            new_post.save()
        return super().form_valid(form)


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = 'blog/blog_details.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count = int(self.object.views_count) + 1
        self.object.save()
        return self.object


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')