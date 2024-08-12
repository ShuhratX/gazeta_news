from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.response import Response

from api.models import Article, Category
from api.serializers import ArticleSerializer
from news.check_news import fetch_news


class ArticlesView(generics.GenericAPIView):

    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category',]

    def get(self, request):
        qst = self.get_queryset()
        qst = self.filter_queryset(qst)
        serializer = self.get_serializer(instance=qst, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        articles = fetch_news()
        created_articles = []

        for article in articles:
            serializer = ArticleSerializer(data=article)
            if serializer.is_valid():
                category = Category.objects.get(name=article['category'])
                saved_article = serializer.save(category=category)
                created_articles.append(saved_article)

        if created_articles:
            return Response({"Qo'shilgan maqolalar": [article.title for article in created_articles]},
                            status=status.HTTP_201_CREATED)
        return Response({"message": "Yangi maqolalar topilmadi."}, status=status.HTTP_200_OK)


class ArticleDetailView(generics.RetrieveAPIView):

    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class ArticleUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class ArticleDeleteView(generics.DestroyAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()