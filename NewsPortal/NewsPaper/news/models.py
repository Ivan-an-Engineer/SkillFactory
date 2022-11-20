from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Author(models.Model):
    author_user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rating = models.IntegerField(default=0)
    author_category = models.ManyToManyField('Category', through='Subscribers')

    def update_rating(self):
        self.author_rating = 0
        for _post in Post.objects.filter(post_author=self):
            self.author_rating += _post.post_rating * 3
            for _comment in Comment.objects.all():
                self.author_rating += _comment.comment_rating
        for _comment in Comment.objects.filter(comment_user=self.author_user):
            self.author_rating += _comment.comment_rating
        self.save()

    def __str__(self):
        return f'{self.author_user.username} *{self.author_rating}*'


class Category(models.Model):
    title = models.CharField(max_length=31, unique=True)

    def __str__(self):
        return f'{self.title}'


class Post(models.Model):
    post_author = models.ForeignKey('Author', on_delete=models.CASCADE)

    post_category = models.ManyToManyField('Category', through='PostCategory')

    post_title = models.CharField(max_length=127)
    post_text = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    post_rating = models.IntegerField(default=0)

    def preview(self):
        return self.post_text[:124] + '...'

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

    def __str__(self):
        return f'{self.post_date.strftime("%d.%m.%Y")} - {self.post_author.author_user.username}: {self.post_title}'


class News(Post):
    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])


class Article(Post):
    def get_absolute_url(self):
        return reverse('articles_detail', args=[str(self.id)])


class PostCategory(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post.id}.{self.post.post_author.author_user.username}: {self.post.post_title} - {self.category}'


class Comment(models.Model):
    comment_post = models.ForeignKey('Post', on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()

    def __str__(self):
        return f'{self.comment_user.username}: {self.comment_text} *{self.comment_rating}*'


class Subscribers(models.Model):
    user = models.ForeignKey('Author', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.category.title}'
