from django.db import models

# Create your models here.


class UserRegistraionModel(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=200)

    class Meta:
        db_table = 'tbl_ragistration'

    def __str__(self):
        return self.user_name


class NewProductAddModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    images = models.FileField(upload_to='img/')
    price = models.CharField(max_length=100)
    discount = models.CharField(max_length=100)

    class Meta:
        db_table = 'tbl_product_add'

    def __str__(self):
        return self.title
