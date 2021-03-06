from django.db import models


class Review(models.Model):
    user_name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.IntegerField()
    owner_comment = models.TextField(default="")

    def __str__(self):
        return self.user_name
