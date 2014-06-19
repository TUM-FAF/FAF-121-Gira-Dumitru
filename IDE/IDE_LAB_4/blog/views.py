from blog.models import Blog
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    return render_to_response('index.html', {

        'posts': Blog.objects.all()[:5]
    })


