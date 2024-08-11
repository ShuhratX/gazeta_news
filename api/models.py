from django.db import models


class Category(models.Model):
    class Meta:
        db_table = "categories"

    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name


class Article(models.Model):
    class Meta:
        db_table = "articles"

    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name="articles", on_delete=models.CASCADE)
    content = models.TextField()
    link = models.CharField(max_length=255)
    pub_date = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
