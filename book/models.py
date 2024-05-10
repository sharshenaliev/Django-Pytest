from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название жанра')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя автора')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey("account.MyUser", on_delete=models.CASCADE, verbose_name='Автор отзыва')
    book_object = models.ForeignKey('Book', on_delete=models.PROTECT, verbose_name='Книга')
    rating = models.PositiveIntegerField(verbose_name='Рейтинг', validators=[MaxValueValidator(10), MinValueValidator(0)])
    text = models.TextField(verbose_name='Текст отзыва')

    class Meta:
        unique_together = ('user', 'book_object')
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'{self.user}: {self.book_object} - {self.rating}'


class Book(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name="URL")
    description = models.TextField(verbose_name='Описание')
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, verbose_name='Жанр')
    author = models.ForeignKey(Author, on_delete=models.PROTECT, verbose_name='Автор')
    date = models.DateField(auto_now_add=True, verbose_name='Дата публикации')
    reviews_list = models.ManyToManyField(Review, verbose_name='Список отзывов', blank=True, null=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.name
