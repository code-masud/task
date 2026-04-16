from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.generic import TemplateView, DetailView
from .models import *
from .utils import highlight_terms


class HomeView(TemplateView):
    template_name = 'task/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["articles"] = Article.objects.all()
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'task/article_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        article = context['article']
        article.description = highlight_terms(article.description)

        categories = Category.objects.all()

        for cat in categories:
            cat.description = highlight_terms(cat.description)

        context['categories'] = categories

        return context

def term_detail(request, id):
    term = get_object_or_404(Term, id=id)

    contents = term.contents.all()

    data = []
    for c in contents:
        data.append({
            "type": c.type,
            "title": c.title,
            "text": c.text,
            "file": c.file.url if c.file else "",
            "youtube_id": c.youtube_id
        })

    return JsonResponse({
        "word": term.word,
        "contents": data
    })


def content_detail(request, id):
    block = get_object_or_404(ContentBlock, id=id)

    return JsonResponse({
        "type": block.type,
        "title": block.title,
        "text": block.text,
        "file": block.file.url if block.file else "",
        "youtube_id": block.youtube_id,
    })
