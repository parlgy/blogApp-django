from dataclasses import field
from re import template
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin




# function based views
def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context)


# it supports the above function based views
# class based views
# the variables template_name, context_object_name, ordering are set because the exact conventions/ rules / files that the,
# view was looking for was not correct.
# class based views looks of a file of type <app>/<models>/<viewtype>.html

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<models>/<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

# class based view for the details of an individual post
#it follows the correct conventions and therefore no variables need to be initialised
class PostDetalView(DetailView):
    model = Post
    
# view for creating post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post

    # Fields to be added in the form
    fields = ['title', 'content']

    # override form valid method
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# view for updating a post
# it inherits from the UserPassesTestMixin class
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # override form valid method
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # override test_func method
    # this method is used to check if the user is the author of the post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# this view is used to delete a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # redirect to home page after successful deletion
    success_url = '/' 

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# View for about Page
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})