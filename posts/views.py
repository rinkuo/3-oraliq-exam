import random
from django.shortcuts import render, get_object_or_404, redirect
from tags.models import Tag
from django.db.models import Count
from catalogs.models import Category
from .models import Post, Comment
from .forms import CommentForm

def home(request):
    return render(request, 'posts/index_with_side_bar.html')

def post_list(request):
    posts = Post.objects.annotate(comments_count=Count('comments'))
    selected_categories = request.GET.getlist('category')
    selected_tags = request.GET.getlist('tag')
    sort_by = request.GET.get('sort', '')
    search_query = request.GET.get('search', '')
    start_date = request.GET.get('start_date', None)
    end_date = request.GET.get('end_date', None)

    if 'all' in selected_categories:
        posts = Post.objects.all()
    elif selected_categories:
        posts = posts.filter(category__slug__in=selected_categories)

    if selected_tags:
        posts = posts.filter(tag__slug__in=selected_tags)

    if search_query:
        posts = posts.filter(name__icontains=search_query)

    if start_date:
        posts = posts.filter(created_at__date__gte=start_date)
    if end_date:
        posts = posts.filter(created_at__date__lte=end_date)

    if sort_by == 'latest':
        posts = posts.order_by('-created_at')
    elif sort_by == 'oldest':
        posts = posts.order_by('created_at')
    elif sort_by == 'popular':
        posts = posts.order_by('-comments_count')

    tags = sorted(
        Tag.objects.all(),
        key=lambda t: (t.slug not in selected_tags, t.name)
    )
    categories = sorted(
        Category.objects.all(),
        key=lambda c: (c.slug not in selected_categories, c.name)
    )

    colors = ['blue', 'green', 'red', 'purple', 'orange', 'yellow']

    posts_with_read_time = []
    for post in posts:
        random_read_time = round(random.uniform(1, 10), 1)
        post.read_time = random_read_time
        posts_with_read_time.append(post)

    ctx = {
        'posts': posts_with_read_time,
        'categories': categories,
        'tags': tags,
        'selected_categories': selected_categories,
        'selected_tags': selected_tags,
        'current_sort': sort_by,
        'search_query': search_query,
        'start_date': start_date,
        'end_date': end_date,
        'colors': colors,
    }

    return render(request, 'posts/index_with_side_bar.html', ctx)

def blog_detail(request, year, month, day, slug):
    post = get_object_or_404(
        Post,
        slug=slug,
        created_at__year=year,
        created_at__month=month,
        created_at__day=day
    )

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post.get_detail_url())
    else:
        form = CommentForm()

    comments = Comment.objects.filter(post=post)

    ctx = {
        'post': post,
        'form': form,
        'comments': comments,
    }

    return render(request, 'posts/post-detail.html', ctx)
