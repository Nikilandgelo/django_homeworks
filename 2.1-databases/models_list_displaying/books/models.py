from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=64, unique = True)
    author = models.CharField(max_length=64)
    pub_date = models.CharField()

    def __str__(self) -> str:
        return self.name + " " + self.author