from django.db import models

# Create your models here.
CATEGORY = [
    ('Mystery', 'Mystery'),
    ('Thriller', 'Thriller'),
    ('Science-Fiction', 'Science-Fiction'),
    ('Humor', 'Humor'),
    ('Horror', 'Horror'),
    ('Biography', 'Biography'),
    ('Historical Fiction', 'Historical Fiction'),
    ]

class BookShopeModel(models.Model):
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    category = models.CharField(max_length=30, choices=CATEGORY)
    first_pub = models.DateTimeField(auto_now_add=True) 
    last_pub = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.book_name
    
