from django.db import models
from datetime import datetime


class Categories(models.TextChoices):
    WORLD = "world"
    POLITICS = "politics"
    TECHNOLOGY = "technology"
    BUSINESS = "business"
    SPORTS = "sports"


class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(
        max_length=50, choices=Categories.choices, default=Categories.WORLD
    )
    excerpt = models.CharField(max_length=150)
    month = models.CharField(max_length=3)
    day = models.CharField(max_length=2)
    content = models.TextField()
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self) -> str:
        return self.title
