# Django Permission Management – Bookshelf Application

This project implements Django’s authentication system using a custom user model and custom permissions for the Book model.

---

# 1. Custom User Model

The application uses a custom user class instead of Django’s default `User`.  

- Location: `bookshelf/models.py`
- Class name: `CustomUser`
- Inherits: `AbstractUser`
- Email is used as the login field
- Includes additional fields:
  - `date_of_birth`
  - `profile_photo`

To activate the custom user model, the Django settings include:

```python
AUTH_USER_MODEL = "bookshelf.CustomUser"
