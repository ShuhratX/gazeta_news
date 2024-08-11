from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from api.models import Article
from api.serializers import ArticleSerializer


class ArticlesCreateView(generics.CreateAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def create(self, request, *args, **kwargs):

        return super(ArticlesCreateView, self).create(request, args, kwargs)


class ArticlesListView(generics.ListAPIView):

    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'created_date']


class ArticleDetailView(generics.RetrieveAPIView):

    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
