# FastAPI Starter Code

# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Example Pydantic model for a resource (e.g., Book)
class Book(BaseModel):
    title: str
    author: str

# In-memory storage for books
books: List[Book] = []

@app.get("/books", response_model=List[Book])
def get_books():
    return books

@app.post("/books", response_model=Book, status_code=201)
def add_book(book: Book):
    books.append(book)
    return book
