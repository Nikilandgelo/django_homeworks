from django.db import models
    
class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(verbose_name='Изображение')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self) -> str:
        return self.title
    
class Tag(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    articles = models.ManyToManyField(Article, through="TagArticles")

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.name

class TagArticles(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='Раздел')
    is_main = models.BooleanField(verbose_name="Основная категория")

    class Meta:
        verbose_name = 'Тематики статьи'
        verbose_name_plural = 'Тематика статьи'
    
    def __str__(self) -> str:
        return f'{self.tag} - {self.article}'