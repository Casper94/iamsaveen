from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request, 'mysite/home.html')

def about(request):
    return render(request, 'mysite/about.html')


def resume(request):
    return render(request, 'mysite/resume.html')


def skills(request):
    return render(request, 'mysite/skills.html')


def services(request):
    return render(request, 'mysite/services.html')


def projects(request):
    return render(request, 'mysite/projects.html')

def contact_me(request):
    return render(request, 'mysite/contact_me.html')

def categoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'mysite/categories.html', {'cats': cats.replace('-', ' '), 'category_posts': category_posts})


class BlogHomeView(ListView):
    model = Post
    template_name = 'mysite/myblog.html'
    ordering = ['-date_posted']

class BlogPostDetailView(DetailView):
    model = Post
    template_name = 'mysite/post_detail.html'

    def get_context_data(self, *args, **kwargs):
        cat_list = Category.objects.all()
        recent_blogs = Post.objects.all()
        context = super(BlogPostDetailView, self).get_context_data(*args, **kwargs)
        context["cat_list"] = cat_list
        context["recent_blogs"] = recent_blogs
        return context

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'mysite/post_detail.html'
    success_url = reverse_lazy('blog')

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.get_object(Post.objects.all().pk)})

class PostCommentView(View):
    def get(self, request, *args, **kwargs):
         view = BlogPostDetailView.as_view()
         return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs) :
         view = AddCommentView.as_view()
         return view(request, *args, **kwargs)

class AddBlogPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'mysite/add_post.html'
    # fields = ('title', 'author', 'content')



class AddCategoryView(CreateView):
    model = Category
    template_name = 'mysite/add_category.html'
    fields = '__all__'


class UpdateBlogPostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'mysite/update_post.html'
    # fields = ('title', 'title_tag', 'snippet', 'content')

class DeletePostView(DeleteView):
    model = Post
    template_name = 'mysite/delete_post.html'
    success_url = reverse_lazy('blog')

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            url = self.success_url
            return HttpResponseRedirect(url)
        else:
            return super(DeletePostView, self).post(request, *args, **kwargs)