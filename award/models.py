from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=True)
    profile_picture = models.ImageField(upload_to='user/')

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['first_name']

    def save_user(self):
        self.save()

    @classmethod
    def update_user(cls, id, new_First_Name):
        cls.objects.filter(user_id=id).update(First_name=new_first_Name)
        new_title_object = cls.objects.get(First_Name=new_first_Name)
        new_name = new_title_object.first_Name
        return new_name
    
    @classmethod
    def get_user_profile(cls,id):
        profile = cls.objects.get(user_id=id)
        return profile




class Post(models.Model):
    title = models.CharField(max_length=30)
    description = HTMLField()
    link = models.CharField(max_length=500)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()
    
    

    def search_by_title(cls, search_term):
        award = cls.objects.filter(title__icontains=search_term)
        return award


class AwardLetterRecipients(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()

class Rating(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    description = models.TextField()
    review = models.CharField(max_length=200)