from rest_framework.generics import ListAPIView
from ..serializers import AuthorSerializer
from ..models import Author


class AuthorList(ListAPIView):
    serializer_class = AuthorSerializer

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.GET = None

    def get_queryset(self):
        data = self.GET
        return Author.objects.filter(first_name=data["first_name"], last_name=data["last_name"])
