from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# ==========================
# CUSTOM USER MANAGER
# ==========================
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)


# ==========================
# CUSTOM USER MODEL
# ==========================
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profiles/', null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username


# ==========================
# AUTHOR MODEL
# ==========================
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# ==========================
# BOOK MODEL
# ==========================
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books", null=True, blank=True)

    class Meta:
        permissions = [
            ("can_view", "Can view books"),
            ("can_create", "Can create books"),
            ("can_edit", "Can edit books"),
            ("can_delete", "Can delete books"),
        ]

    def __str__(self):
        return self.title
