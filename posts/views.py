from django.shortcuts import render
from django.urls import reverse_lazy

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.shortcuts import render, redirect
from .forms import BlogPostForm


from posts.models import BlogPost

class BlogHome(ListView):
    model = BlogPost
    context_object_name = 'posts'
    
    # La methode get_queryset est une methode qui est une methode qui permet de recuperer les données dans la base de donnée selon les status de publication.
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True)
    
@method_decorator(login_required, name="dispatch")    
class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = 'posts/blogpost_create.html'
    fields = ["title", "content", 'published', 'thumbnail' ]

#  @method_decorator(login_required, name="dispatch")             
class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = 'posts/blogpost_edit.html'
    fields = ['title', 'content', 'published', 'thumbnail' ]

# @method_decorator(login_required, name="dispatch")  
class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = "post"

# @method_decorator(login_required, name="dispatch")  
class BlogPostDelete(DeleteView):
    model = BlogPost
    context_object_name = "post"
    success_url = reverse_lazy('posts:home')


def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)  # gérer request.FILES pour les images
        if form.is_valid():
            form.save()
            return redirect('posts:home')  # ou autre url de redirection
    else:
        form = BlogPostForm()
    return render(request, 'blogpost_create.html', {'form': form})
