from django.urls import path
from .views import home, BookView, AuthorView
urlpatterns = [
    path('', home, name='home'),
    path('books/', BookView.as_view(), name='books'),
    path('books/<int:pk>/', BookView.as_view(), name='book'),
    path('authors/', AuthorView.as_view(), name='authors'),
    path('authors/<int:pk>/', AuthorView.as_view(), name='author'),
    ]
