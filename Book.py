from django.db import models
class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        abstract = true
class Book(models.Model):
    name = models.CharField(max_length=100)
    qty = models.ItrgerField()
    price = models.FloatField()
    category = models.CharField(Max_length=100)
    author = models.CharField(max_length=100)
    class Meta:
        db_table = 'Book_info '


    class publication(models.Model):
        name = models.CharField(Max_length=100)
        address = models.CharField(Max_length=100)
        email = models.EmailField()

        class Meta:
            db_tsble = 'Publicatio_info'

    class Author(models.Model):
        name = models.CharField(Max_length=100)
        addres = models.CharField(Max_length=100)
        email = models.EmailField()
        clasa Meta:
        db_table = 'Author_info'