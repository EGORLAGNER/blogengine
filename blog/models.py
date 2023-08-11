from django.db import models
from django.shortcuts import reverse

from django.utils.text import slugify
from time import time


def gen_slug(string):
    slug = slugify(string, allow_unicode=True)
    return slug + '-' + str(int(time()))


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    body = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    data_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'


class Tag(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, unique=True)

    """
    get_absolute_url возвращает полный URL адрес до экземпляра.
    название 
    """

    def get_absolute_url(self):
        result = reverse('tag_detail_url', kwargs={'slug': self.slug})
        return result

    def __str__(self):
        return f'{self.title}'
