from django.test import TestCase
from .models import User, Post, categories

# Create your tests here.


class UserTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james = User(first_name='James', last_name='Muriuki',
                          email='james@moringaschool.com')

        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james, User))

        # Testing Save Method
    def test_save_method(self):
        self.james.save_user()
        users = User.objects.all()
        self.assertTrue(len(users) > 0)


class PostTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.james = User(first_name='James', last_name='Muriuki',
                          email='james@moringaschool.com')
        self.james.save_user()

        # Creating a new tag and saving it
        self.new_categories = categories(categories='testing')
        self.new_categories.save()

        self.new_post = Post(title='Test Post', post='This is a random test Post',user=self.james)
        self.new_post.save()

        self.new_post.categories.add(self.new_categories)

    def tearDown(self):
        User.objects.all().delete()
        categories.objects.all().delete()
        Post.objects.all().delete()

       
