from django.urls import path
from api.views import ArticlesView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView

urlpatterns = [
    path('check/', ArticlesView.as_view()),
    path('detail/<int:pk>/', ArticleDetailView.as_view()),
    path('update/<int:pk>/', ArticleUpdateView.as_view()),
    path('delete/<int:pk>/', ArticleDeleteView.as_view())

]