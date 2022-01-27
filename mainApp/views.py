from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from .models import Post, Author
from datetime import datetime
from .filters import *
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail



@login_required
def upgrade_me(request):
    user = request.user
    user_obj = User.objects.get(username=user.username)
    premium_group = Group.objects.get(name='author')
    if not request.user.groups.filter(name='author').exists():
        premium_group.user_set.add(user)
        Author.objects.create(author=user_obj)
    return redirect('/')


class PostList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'mainApp/news.html'
    queryset = Post.objects.all()
    context_object_name = 'news'
    paginate_by = 10
    ordering = ['-dateCreation']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['all_news'] = Post.objects.all()
        context['is_not_author'] = not self.request.user.groups.filter(
            name='author').exists()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'mainApp/news_detail.html'
    context_object_name = 'news_detail'


def search(request):
    f = SearchFilter(request.GET, queryset=Post.objects.all())
    return render(request, 'mainApp/search.html', {'filter': f})


class NewsCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    template_name = 'mainApp/add_news.html'
    permission_required = ('mainApp.add_post')
    form_class = PostForm
    success_url = '/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = Author.objects.get(author=self.request.user)
        self.object.save()
        
        cat = Category.objects.get(pk=self.request.POST['postCategory'])
        self.object.postCategory.add(cat)
        return super().form_valid(form)


class NewsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'mainApp/update_news.html'
    form_class = PostForm
    success_url = '/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'mainApp/delete_post.html'
    queryset = Post.objects.all()
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author.author:
            return True
        return False


class CategorySubscribe(DetailView):
    model = Category
    template_name = 'mainApp/post_category.html'
    context_object_name = 'post_category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@login_required
def subscribe_category(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)
    send_mail(
        f'{category.name}',
        f' {request.user}! Вы подписались на обновление категории: «{category.name}».',
        '',
        [user.email],
        fail_silently=False,
    )
    return redirect('home')


@login_required
def unsubscribe_category(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.remove(user)
    send_mail(
        subject=f'{category}',
        message=f'Вы «{request.user}» отписались от обновлений категории: «{category}».',
        from_email='',
        recipient_list=['', ],
    )
    return redirect('/news')
