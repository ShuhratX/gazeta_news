from rest_framework import serializers
from .models import Article, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'link', 'pub_date', 'category']

    def create(self, validated_data):

        # Ma'lumot qatorining mavjudligini tekshirish
        if Article.objects.filter(title=self.validated_data['title']).first():
            return None
        else:
            # Agar mavjud bo'lmasa, yangi qator yaratamiz
            return super().create(validated_data)