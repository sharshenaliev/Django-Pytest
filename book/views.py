from rest_framework.generics import (RetrieveAPIView, ListAPIView, RetrieveDestroyAPIView,
                                     CreateAPIView, DestroyAPIView)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from book.filters import DateFilter
from django.db.models import Exists, OuterRef, Avg
from book.serializers import *
from book.models import Book
from book.permissions import IsOwner


class BookListView(ListAPIView):
    serializer_class = BookListSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = DateFilter
    search_fields = ['name', ]

    def get_queryset(self):
        queryset = Book.objects.annotate(
            is_favorite=Exists(self.request.user.favorite.filter(pk=OuterRef('pk'))),
            average_rating=Avg("reviews_list__rating", default=0)
        ).select_related('genre', 'author').order_by('-id')
        return queryset


class BookDetailView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookDetailSerializer
    queryset = Book.objects.all().prefetch_related('reviews_list').select_related('genre', 'author')


class BookFavoriteView(RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        print(instance)
        user.favorite.add(instance)
        return Response({"message": "add to favorite"})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        user.favorite.remove(instance)
        return Response({"message": "remove from favorite"})


class ReviewCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        data['user'] = request.user.pk
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save(user=request.user)
        instance.book_object.reviews_list.add(instance)
        return Response(serializer.data)


class ReviewDestroyView(DestroyAPIView):
    permission_classes = (IsOwner,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
