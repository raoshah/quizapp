
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)  # Save the user to generate an id
        group = Group.objects.get(name='test')  # Replace 'test' with the actual group name
        user.groups.add(group)  # Add user to group after saving
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='users')
    post = models.CharField(max_length=240)


class QuizCategory(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name



class Question(models.Model):
    ANSWER_CHOICES = (("A", "a"),("B", "b"),("C", "c"),("D", "d"))   
    category = models.ForeignKey(QuizCategory, on_delete=models.CASCADE, related_name='quiz_category')
    question = models.CharField(max_length=1000)
    a = models.CharField(max_length=1000)
    b = models.CharField(max_length=1000)
    c = models.CharField(max_length=1000)
    d = models.CharField(max_length=1000)
    answer = models.CharField(max_length=4,choices=ANSWER_CHOICES,default="A")