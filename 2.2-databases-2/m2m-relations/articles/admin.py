from django.contrib import admin
from django.forms import BaseInlineFormSet, ValidationError
from articles.models import Article, Tag, TagArticles

class RelationshipInlineFormset(BaseInlineFormSet):
    
    def clean(self) -> None:
        one_main = False
        for element in self.cleaned_data:
            if element.get("is_main") == True:
                if one_main == False:
                    one_main = True
                else:
                    raise ValidationError("Основным может быть только один раздел")
        
        if one_main == False:
            raise ValidationError("Укажите основной раздел")
        
        return super().clean()

class TagArticleInLine(admin.TabularInline):
    model = TagArticles
    extra = 0
    formset = RelationshipInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagArticleInLine]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass