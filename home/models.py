from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify
# Create your models here.

class Base(models.Model):
    class Meta:
        abstract = True

    create_date = models.DateTimeField( auto_now_add= True )
    update_date = models.DateTimeField( auto_now= True )

class Contact(Base):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    subject = models.IntegerField(choices=[(1, 'Teklif'), (2, 'Irad'), (3, 'Sikayet')])
    message = models.TextField()
    create_date = models.DateTimeField( auto_now_add= True )
    update_date = models.DateTimeField( auto_now= True )
    def __str__(self) -> str:
        return self.name


class Subscribe(Base):
    email = models.EmailField(max_length=50, unique= True)
    def __str__(self) -> str:
        return self.email
    

class Category(Base):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='category/')
    slug = models.SlugField(max_length=50, null = True, blank = True)

    # def save(self, *args, **kwargs) -> None:
    #     self.slug = slugify(f'{self.name}')
    #     return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
    

class Tag(Base):
    name = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.name

class Strories(Base):
    user = models.ForeignKey(User, related_name = 'strories', on_delete = models.CASCADE )
    category = models.ForeignKey(Category, related_name= 'strories', on_delete = models.CASCADE )
    tag = models.ManyToManyField(Tag, related_name= 'strories')
    image = models.ImageField(upload_to = 'strories/')
    cover_image = models.ImageField(upload_to = 'strories/cover_image/')
    title = models.CharField(max_length = 30 ) 
    desc = RichTextField()
    slug = models.SlugField(max_length = 50, null=True, blank= True)

    # def save(self, *args, **kwargs) -> None:
    #     self.slug = slugify(f'{self.title} {self.id}')
    #     return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
    

class Comment(Base):
    stories = models.ForeignKey(Strories, related_name='comment', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comment', on_delete=models.CASCADE)
    # reply = models.ForeignKey('self', null = True, blank = True, related_name='child', on_delete=models.CASCADE)
    comment = models.TextField()

    # def __str__(self) -> str:
    #     return f"{self.user.username} -- {self.comment[:10]}"

