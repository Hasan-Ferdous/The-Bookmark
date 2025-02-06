import requests
from django.shortcuts import render, get_object_or_404
from .models import Book, Review

def fetch_book_cover(title):
    """Fetches book cover from Open Library API"""
    search_url = f"https://openlibrary.org/search.json?title={title}"
    response = requests.get(search_url)
    data = response.json()
    
    if "docs" in data and len(data["docs"]) > 0:
        book_data = data["docs"][0]
        if "cover_i" in book_data:
            return f"https://covers.openlibrary.org/b/id/{book_data['cover_i']}-L.jpg"
    return None  # No cover found

def book_list(request):
    books = Book.objects.all()
    for book in books:
        if not book.cover_url:  # Only fetch if cover is not already set
            cover = fetch_book_cover(book.title)
            if cover:
                book.cover_url = cover
                book.save()

    return render(request, "reviews/book_list.html", {"books": books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    reviews = Review.objects.filter(book=book)
    
    if not book.cover_url:  # Fetch cover if not already set
        cover = fetch_book_cover(book.title)
        if cover:
            book.cover_url = cover
            book.save()
    
    return render(request, "reviews/book_detail.html", {"book": book, "reviews": reviews})
