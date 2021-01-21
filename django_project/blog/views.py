from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    

)
from .models import Post
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html',context)
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'      #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','categories','content']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','categories','content']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False




def about(request):
    return render(request,'blog/about.html')
def announcement(request):
    return render(request,'blog/announcement.html')

def LikeView(request, pk):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))
    Post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post_detail',args=[str(pk)]))