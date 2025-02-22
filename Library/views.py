import json
from .models import Book, Author, Category, Publisher
from django.views import View
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .serializers import BookSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, permissions
from rest_framework.response import Response


def home(request):
    return HttpResponse("Welcome!")

@method_decorator(csrf_exempt, name='dispatch')
class BookView(View):
    def get(self, request, pk=None):
        if pk:
            book = get_object_or_404(Book, id=pk)
            return JsonResponse({
                'id': book.id,
                'title': book.title,
                'author': book.author.name,
                'category': book.category.name,
                'description': book.description,
                'published_date': book.published_date,
                'isbn': book.isbn,
                'available_copies': book.available_copies,
            })
        else:
            books = list(Book.objects.values())
            return JsonResponse(books, safe=False)


    def post(self, request):
        try:
            data = json.loads(request.body)
            book = Book.objects.create(**data)
            return JsonResponse({
                'id': book.id,
                'title': book.title,
                'author': book.author.name,
                'category': book.category.name,
                'description': book.description,
                'published_date': book.published_date,
                'isbn': book.isbn,
                'available_copies': book.available_copies,
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    def put(self, request, pk):
        try:
            book = get_object_or_404(Book, id=pk)
            data = json.loads(request.body)
            for key, value in data.items():
                setattr(book, key, value)
            book.save()
            return JsonResponse({
                'id': book.id,
                'title': book.title,
                'author': book.author.name,
                'category': book.category.name,
                'description': book.description,
                'published_date': book.published_date,
                'isbn': book.isbn,
                'available_copies': book.available_copies,
            })
        except book.DoesNotExist:
            return JsonResponse({'error': 'Book not found'}, status=404)

    def delete(self, request, pk):
        try:
            book = get_object_or_404(Book, id=pk)
            book.delete()
            return JsonResponse({'message': 'Book deleted successfully'})
        except book.DoesNotExist:
            return JsonResponse({'error': 'Book not found'}, status=404)

@method_decorator(csrf_exempt, name='dispatch')
class AuthorView(View):
    def get(self, request, pk=None):
        if pk:
            author = get_object_or_404(Author, id=pk)
            return JsonResponse({
                'id': author.id,
                'name': author.name,
                'place_of_birth': author.place_of_birth,
                'no_of_books': author.no_of_books,
                'publisher': author.publisher.name if author.publisher else None,
            })
        else:
            authors = list(Author.objects.values())
            return JsonResponse(authors, safe=False)
        
# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticated]

#     def list(self, request):
#         books = self.get_queryset()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, pk=None):
#         book = self.get_object()
#         serializer = self.get_serializer(book)
#         return Response(serializer.data)

#     def update(self, request, pk=None):
#         book = self.get_object()
#         serializer = self.get_serializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):
#         book = self.get_object()
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
