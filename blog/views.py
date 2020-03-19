from django.shortcuts import render

# Create your views here.
from .models import Post
from django.views.generic import ListView,DeleteView

class PostListView(ListView):
    queryset = Post.objects.all().order_by("-datetime")
    template_name = 'blog/blog.html'
    context_object_name = "Post"
    paginate_by = 2
def post(request,id):
    post = Post.objects.get(id = id)
    return render(request,'blog/post.html',{"post":post})