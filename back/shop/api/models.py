from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    homeMade = models.BooleanField()

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'address': self.address,
            'homeMade': self.homeMade
        }


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField(default=255)
    company = models.ForeignKey(Company,
                                on_delete=models.RESTRICT,
                                related_name='ID')
    sold = models.BooleanField(default=False)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'company': self.company.name,
            'homeMade': self.company.homeMade,
            'sold': self.sold
        }