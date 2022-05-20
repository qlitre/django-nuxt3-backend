from django.db import models
from django.utils import timezone
from mdeditor.fields import MDTextField


class Category(models.Model):
    """カテゴリ"""
    name = models.CharField('カテゴリ名', max_length=32)
    slug = models.SlugField('スラッグ', max_length=32)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """タグ"""
    name = models.CharField('タグ名', max_length=32)
    slug = models.SlugField('スラッグ', max_length=32)

    def __str__(self):
        return self.name


class Post(models.Model):
    """記事"""
    title = models.CharField('タイトル', max_length=40)
    slug = models.SlugField('スラッグ', max_length=40)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='カテゴリ')
    tag = models.ManyToManyField(Tag, verbose_name='タグ', blank=True)
    thumbnail = models.ImageField('サムネイル', blank=True, null=True)
    description = models.TextField('紹介文')
    main_text = MDTextField()
    created_at = models.DateTimeField('作成日', default=timezone.now)
    is_public = models.BooleanField('公開可能フラグ', default=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title


class About(models.Model):
    profile_image = models.ImageField('プロフィール画像')
    body = MDTextField()
