from django.db import models
from django.utils import timezone
from django.shortcuts import reverse

class Post(models.Model):
    title=models.CharField("Название", max_length=255)
    slug=models.SlugField("Ссылка", unique=True)
    text=models.TextField("Текст")
    image=models.ImageField("Картинка", upload_to="post_img/")
    date=models.DateTimeField("Дата публикации", default=timezone.now)
    

    def get_link(self):
        return reverse("post_detail_url", kwargs={"slug": self.slug})    
    
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title
    
class Product(models.Model):
    title=models.CharField("Название", max_length=255)
    image=models.ImageField("Картинка", upload_to="product_img/")
    description=models.TextField("Описание")
    slug=models.SlugField("Ссылка", unique=True)
    
    def get_link(self):
        return reverse("product_detail_url", kwargs={"slug": self.slug})    
    
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.title
