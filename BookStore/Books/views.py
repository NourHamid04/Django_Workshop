from ninja import NinjaAPI
from django.shortcuts import get_object_or_404
from .models import Author, Book
from .schemas import (
    AuthorSchema, AuthorCreateSchema,
    BookSchema, BookCreateSchema
)

api = NinjaAPI()

# Author Endpoints

@api.get("/authors", response=list[AuthorSchema])
def list_authors(request):
    return Author.objects.all()


@api.post("/authors", response=AuthorSchema)
def create_author(request, payload: AuthorCreateSchema):
    author = Author.objects.create(**payload.dict())
    return author

@api.get("/authors/{author_id}", response=AuthorSchema)
def get_author(request, author_id: int):
    return get_object_or_404(Author, id=author_id)

@api.put('/authors/{author_id}', response=AuthorSchema)
def update_author(request, author_id: int, payload: AuthorCreateSchema):
    author = Author.objects.get(id=author_id)
    author.name = payload.name
    author.save()

    return author

@api.delete("/authors/{author_id}")
def delete_author(request, author_id: int):
    author = get_object_or_404(Author, id=author_id)
    author.delete()
    return {"success": True}

# Book Endpoints

@api.get("/books", response=list[BookSchema])
def list_books(request):
    return Book.objects.select_related('author').all()

@api.post("/books", response=BookSchema)
def create_book(request, payload: BookCreateSchema):
    author = get_object_or_404(Author, id=payload.author_id)
    book = Book.objects.create(
        title=payload.title,
        description=payload.description,
        author=author
    )
    return book

@api.get("/books/{book_id}", response=BookSchema)
def get_book(request, book_id: int):
    return get_object_or_404(Book, id=book_id)

@api.put("/books/{book_id}", response=BookSchema)
def update_book(request, book_id: int, payload: BookCreateSchema):
    book = get_object_or_404(Book, id=book_id)
    author = get_object_or_404(Author, id=payload.author_id)
    book.title = payload.title
    book.description = payload.description
    book.author = author
    book.save()
    return book

@api.delete("/books/{book_id}")
def delete_book(request, book_id: int):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return {"success":True}