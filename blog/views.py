from django.shortcuts import render

# Create your views here.


def main_page(request):
    return render(request, 'blog/index.html')


def posts(request):
    return render(request, 'blog/all-posts.html')


def post(request, slug):
    return render(request, 'blog/post-detail.html')
