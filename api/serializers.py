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
        fields = ['id', 'title', 'content', 'link', 'pub_date', 'category', 'created_date']

    def validate(self, data):
        # Ma'lumot qatorining mavjudligini tekshirish
        if Article.objects.filter(title=data['title']).exists():

            raise serializers.ValidationError("Ushbu maqola ma'lumotlar bazasida mavjud.")
        return data

