from django.db import models

class Phone(models.Model):
    name = models.CharField(max_length = 50, unique = True)
    price = models.IntegerField()
    image = models.CharField(max_length = 500)
    release_date = models.CharField(max_length = 10)
    lte_exists = models.BooleanField()
    slug = models.SlugField()

    def __str__(self) -> str:
        return self.name