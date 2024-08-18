from django.shortcuts import render
from .models import Blogpost
from django.http import HttpResponse



def index(request):
    allposts = Blogpost.objects.all()
    print(allposts)
    return render(request, 'eread/index.html', {'allposts':allposts})

def blogpost(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]
    print(post)
    return render(request, 'eread/blogpost.html',{'post':post})
