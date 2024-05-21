from django.db import models

# Create your models here.

class Publishing_House(models.Model):

    title = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    date_of_opening = models.DateField()
    website = models.URLField()

    def __str__(self):
        return self.title


class Book(models.Model):

    Types = [
        ("SF", "Soft"),
        ("HR", "Hard")
    ]

    Categories = [
        ("ROM", "Romance"),
        ("TRI", "Thriller"),
        ("BIO", "Biography"),
        ("CLS", "Classic"),
        ("DRA", "Drama"),
        ("HIS", "History")
    ]

    title = models.CharField(max_length=200)
    image = models.ImageField()
    isbn = models.CharField(max_length=100)
    year_of_publish = models.DateField()
    number_of_pages = models.IntegerField()
    dimension_of_book = models.CharField(max_length=80)
    type_of_book = models.CharField(max_length=3, choices=Types)
    category = models.CharField(max_length=4, choices=Categories)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    publishing_house = models.ForeignKey(Publishing_House, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
