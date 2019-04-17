from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from book.models import Book
from .serializers import BookSerializer

# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    '''BookオブジェクトのCRUDを行うAPI'''

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )