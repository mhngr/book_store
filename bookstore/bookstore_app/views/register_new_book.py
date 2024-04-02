from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from ..serializers import BookSerializer
from ..models import Book


class RegisterNewBook(CreateAPIView):
    serializer_class = BookSerializer

    def _get_book(self, *args, **kwargs):
        try:
            pk = int(self.kwargs.get('pk'))
            return Book.objects.get(pk=pk)
        except Exception:
            return None

    queryset = Book.objects.all()
