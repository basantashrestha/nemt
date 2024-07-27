from django.db import models
class Item(models.Model):
    word = models.CharField(max_length=100)
    wordTrans = models.CharField(max_length=100)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.word

