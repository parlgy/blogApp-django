from django import views
from django.urls import path
from . import views
from .views import PostListView, PostDetalView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetalView.as_view(), name='post-detail'), #looks for post_detail.html
    path('post/new/', PostCreateView.as_view(), name='post-create'),   #looks for post_form.html
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), #it uses te post_form.html template
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]