from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    author_user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rating = models.IntegerField(default=0)

    def update_rating(self):
        self.author_rating = 0
        for _post in Post.objects.filter(post_author=self):
            self.author_rating += _post.post_rating * 3
            for _comment in Comment.objects.all():
                self.author_rating += _comment.comment_rating
        for _comment in Comment.objects.filter(comment_user=self.author_user):
            self.author_rating += _comment.comment_rating
        self.save()


class Category(models.Model):
    title = models.CharField(max_length=31, unique=True)


class Post(models.Model):
    article = 'AR'
    news = 'NW'

    POSITIONS = [
        (article, 'Статья'),
        (news, 'Новость')
    ]

    post_author = models.ForeignKey('Author', on_delete=models.CASCADE)
    post_choice = models.CharField(max_length=2,
                                   choices=POSITIONS,
                                   default=news)
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


class PostCategory(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


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