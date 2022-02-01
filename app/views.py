from app.models import Book
from rest_framework.viewsets import ModelViewSet
from app.serializers import BookSerializer


class BookViewSet(ModelViewSet):
    """
    ModelViewSetでCRUDを実装
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer