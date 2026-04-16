from django.contrib import admin
from .models import Category, Article, ContentBlock, Term, TermContent


class ContentBlockInline(admin.StackedInline):
    model = ContentBlock
    extra = 1
    fields = ('order', 'title', 'type', 'text', 'file', 'youtube_id')
    ordering = ('order',)


class TermContentInline(admin.StackedInline):
    model = TermContent
    extra = 1
    fields = ('order', 'title', 'type', 'text', 'file', 'youtube_id')
    ordering = ('order',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_per_page = 20


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_filter = ('category',)
    search_fields = ('title',)
    inlines = [ContentBlockInline]
    list_per_page = 20


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ('word',)
    search_fields = ('word',)
    inlines = [TermContentInline]
    list_per_page = 20


@admin.register(ContentBlock)
class ContentBlockAdmin(admin.ModelAdmin):
    list_display = ('article', 'type', 'title', 'order')
    list_filter = ('type',)
    search_fields = ('title', 'text')
    ordering = ('article', 'order')


@admin.register(TermContent)
class TermContentAdmin(admin.ModelAdmin):
    list_display = ('term', 'type', 'title', 'order')
    list_filter = ('type',)
    search_fields = ('title', 'text')
    ordering = ('term', 'order')
