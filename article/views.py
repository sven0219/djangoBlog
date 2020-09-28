from django.shortcuts import render
from django.http import HttpResponse
from .models import ArticlePost
import markdown


def article_list(request):
    articles = ArticlePost.objects.all()
    context = {'articles':articles}
    return render(request,'article/list.html',context) 

def article_detail(request,id):
    article = ArticlePost.objects.get(id=id)
    article.body = markdown.markdown(article.body,
        extensions=[
        # 包含 缩写、表格等常用扩展
        'markdown.extensions.extra',
        # 语法高亮扩展
        'markdown.extensions.codehilite',
        ])
    context = { 'article': article }
    return render(request, 'article/detail.html', context)
