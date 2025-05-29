from django.db import models
from django.contrib.auth.models import User


class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='search_history')
    city = models.CharField(max_length=120)
    searched_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-searched_at']

    def __str__(self):
        return f"{self.user.username} искал {self.city} в {self.searched_at}"


class City(models.Model):
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name
