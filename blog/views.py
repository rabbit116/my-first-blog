
# Create your views here.

from django.shortcuts import render


def post_list(request):
    return render(request, 'blog/templates/blog/post_list.html', {})
