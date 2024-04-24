from django.db import models
from django.contrib.auth.models import User

class Advertisement(models.Model):
    
    class Meta:
        verbose_name = 'Обьявление'
        verbose_name_plural = 'Обьявления'
    
    class StatusChoices(models.TextChoices):
        OPEN = "Открыто"
        CLOSED = "Закрыто"

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(choices = StatusChoices.choices, default = StatusChoices.OPEN, max_length = 7, verbose_name='Статус')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='adverts', verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'Обьявление о {self.title} автором {self.creator}'
    

class UserFavouriteAdverts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourite_adverts')
    advertisements = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='in_favourite')