from lib2to3.pgen2.token import TILDE
from re import A
from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def index(request):
    articles = Article.objects.all()
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article()
    article.title = title
    article.content = content
    article.save()

    # article = Article(title=title, content=content)
    # article.save()

    # Article.objects.create(title=title, content=content)


    return redirect('articles:detail', article.pk)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    if request.method == "POST":
        article = Article.objects.get(pk=pk)
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    if request.method == "POST":
        article = Article.objects.get(pk=pk)
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail', article.pk)
    else:
        return redirect('articles:detail', article.pk)
