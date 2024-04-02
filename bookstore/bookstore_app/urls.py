from django.urls import path
from .views import RegisterNewBook, RegisterNewAuthor,AuthorList,BookList

urlpatterns = [
    path("register_new_book", RegisterNewBook.as_view()),
    path("register_new_author", RegisterNewAuthor.as_view()),
    path("list_of_all_books", BookList.as_view()),
    path("list_of_all_authors", AuthorList.as_view())
]