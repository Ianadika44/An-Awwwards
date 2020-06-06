from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=True)
    profile_picture = models.ImageField(upload_to = 'user/')

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['first_name']

    def save_user(self):
        self.save()


class categories(models.Model):
    categories = models.CharField(max_length=50)

    def __str__(self):
        return self.categories

    def save_category(self):
        self.save()


class Post(models.Model):
    title = models.CharField(max_length=60)
    post = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(categories)
    post_image = models.ImageField(upload_to = 'posts/')
    
    def search_by_title(cls,search_term):
        award = cls.objects.filter(title__icontains=search_term)
        return award

class AwardLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()