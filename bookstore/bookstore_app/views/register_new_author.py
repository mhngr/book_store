from rest_framework.generics import CreateAPIView
from ..serializers import AuthorSerializer
from ..models import Author


class RegisterNewAuthor(CreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()