from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    genre = models.CharField(max_length=100)
    cover_url = models.URLField(blank=True, null=True)  # Store cover URL

    def get_cover(self):
        return self.cover_url if self.cover_url else "/static/images/default_cover.jpg"

    def __str__(self):
        return self.title
    
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reviewer = models.CharField(max_length=100)
    rating = models.IntegerField()
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer} - {self.book.title}"
