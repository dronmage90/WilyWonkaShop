from django.db import models
from django.contrib.auth import get_user_model

'''
Model/Table relations
1) OneToOne - each "User" can have only one "Profile"
2) OneToMany - each "Category" can have many "Products"
3) ManyToMany - each "Post" can have many "Tags", in the same time, one "Tag" can in in multiple "Posts"
'''

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             null=True,
                             blank=True)
    home = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.id}: {self.name}'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'home':self.home
        }


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=1000)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    sold = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.name}'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'sold': self.sold,
            'category': self.category.to_json(),
        }
class Commits(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=5)
    text  = models.TextField()

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'text': self.text,
        }