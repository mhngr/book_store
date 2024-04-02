from rest_framework.generics import ListAPIView
from ..serializers import BookSerializer
from ..models import Book


class BookList(ListAPIView):
    serializer_class = BookSerializer

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.GET = None

    def get_queryset(self):
        data = self.GET
        return Book.objects.filter(name=data["name"], author=data["author"])

