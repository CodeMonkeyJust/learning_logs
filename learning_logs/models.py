from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    # 用户学习的主题
    text = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Entry(models.Model):
    # 主题具体知识
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        return self.text[:50] + "..."
