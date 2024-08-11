from django.urls import path
from api.views import ArticlesListView, ArticleDetailView

urlpatterns = [
    path('list/', ArticlesListView.as_view()),
    path('detail/<int:pk>', ArticleDetailView.as_view()),
    path('create/', ArticlesCreateView.as_view()),
]