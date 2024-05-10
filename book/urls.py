from django.urls import path
from book.views import *


urlpatterns = [
    path('book/', BookListView.as_view()),
    path('book/<int:pk>/', BookDetailView.as_view()),
    path('book-favorite/<int:pk>/', BookFavoriteView.as_view()),
    path('review/', ReviewCreateView.as_view()),
    path('review/<int:pk>/', ReviewDestroyView.as_view()),
]
