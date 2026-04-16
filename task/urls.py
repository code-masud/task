from django.urls import path
from . import views

app_name = 'article'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='detail'),
    path('term/<int:id>/', views.term_detail),
    path('content/<int:id>/', views.content_detail),
]
