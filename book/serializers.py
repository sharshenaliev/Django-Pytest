from rest_framework import serializers, validators
from book.models import *


class BookReviewSerializer(serializers.ModelSerializer):
    user_first_name = serializers.CharField(source="user.first_name", read_only=True)

    class Meta:
        model = Review
        exclude = ('book_object', )


class BookListSerializer(serializers.ModelSerializer):
    is_favorite = serializers.BooleanField(read_only=True)
    average_rating = serializers.FloatField(read_only=True)
    genre_name = serializers.CharField(source="genre.name", read_only=True)
    author_name = serializers.CharField(source="author.name", read_only=True)

    class Meta:
        model = Book
        exclude = ('reviews_list', 'description')


class BookDetailSerializer(BookListSerializer):
    reviews = serializers.SerializerMethodField()
    is_favorite = None
    average_rating = None

    class Meta:
        model = Book
        exclude = ('reviews_list', )

    def get_reviews(self, obj):
        reviews = obj.reviews_list.all().select_related('user')
        serializer = BookReviewSerializer(reviews, many=True)
        return serializer.data


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        extra_kwargs = {'user': {'write_only': True}}
